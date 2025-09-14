from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import CustomUser, Book
from .forms import BookForm, UserCreateForm

# ✅ View Users (requires can_view)
@permission_required('bookshelf.can_view', raise_exception=True)
def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, "user_list.html", {"users": users})


# ✅ Create User (secure with form)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_user_view(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully ✅")
            return redirect("user_list")
    else:
        form = UserCreateForm()
    return render(request, "create_user.html", {"form": form})


# ✅ Edit User (secure with form)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        form = UserCreateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully ✅")
            return redirect("user_list")
    else:
        form = UserCreateForm(instance=user)

    return render(request, "edit_user.html", {"form": form, "user": user})


# ✅ Delete User (safe)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_user_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully ❌")
        return redirect("user_list")
    return render(request, "confirm_delete.html", {"user": user})


# ✅ Book list (no change needed, ORM already safe)
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


# ✅ Book detail
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book_detail.html", {"book": book})


# ✅ Create Book (secure with form)
@permission_required('bookshelf.add_book', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully ✅")
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "create_book.html", {"form": form})


# ✅ Edit Book (secure with form)
@permission_required('bookshelf.change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully ✅")
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(request, "edit_book.html", {"form": form, "book": book})


# ✅ Delete Book
@permission_required('bookshelf.delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully ❌")
        return redirect("book_list")
    return render(request, "confirm_delete_book.html", {"book": book})
