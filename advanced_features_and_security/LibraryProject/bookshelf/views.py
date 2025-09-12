from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import CustomUser

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
