from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import CustomUser , Book 

# ✅ View Users (requires can_view)
@permission_required('bookshelf.can_view', raise_exception=True)
def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, "user_list.html", {"users": users})


# ✅ Create User (requires can_create)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_user_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email and password:
            CustomUser.objects.create_user(email=email, password=password)
            messages.success(request, "User created successfully ✅")
            return redirect("user_list")

    return render(request, "create_user.html")


# ✅ Edit User (requires can_edit)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        email = request.POST.get("email")
        date_of_birth = request.POST.get("date_of_birth")

        if email:
            user.email = email
        if date_of_birth:
            user.date_of_birth = date_of_birth

        user.save()
        messages.success(request, "User updated successfully ✅")
        return redirect("user_list")

    return render(request, "edit_user.html", {"user": user})


# ✅ Delete User (requires can_delete)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_user_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully ❌")
        return redirect("user_list")

    return render(request, "confirm_delete.html", {"user": user})


# ✅ BOOK LIST (requires login, but no special permissions)
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


# ✅ BOOK DETAIL VIEW
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book_detail.html", {"book": book})


# ✅ BOOK CREATE (requires permission)
@permission_required('bookshelf.add_book', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("publication_year")

        if title and author and year:
            Book.objects.create(
                title=title,
                author=author,
                publication_year=year
            )
            messages.success(request, "Book created successfully ✅")
            return redirect("book_list")

    return render(request, "create_book.html")


# ✅ BOOK EDIT (requires permission)
@permission_required('bookshelf.change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.title = request.POST.get("title", book.title)
        book.author = request.POST.get("author", book.author)
        book.publication_year = request.POST.get("publication_year", book.publication_year)
        book.save()
        messages.success(request, "Book updated successfully ✅")
        return redirect("book_list")

    return render(request, "edit_book.html", {"book": book})


# ✅ BOOK DELETE (requires permission)
@permission_required('bookshelf.delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully ❌")
        return redirect("book_list")

    return render(request, "confirm_delete_book.html", {"book": book})