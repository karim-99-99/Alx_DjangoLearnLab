from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth.decorators import user_passes_test

# Function-based view
def list_books(request):
    books = Book.objects.all()   # ✅ fetch all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')