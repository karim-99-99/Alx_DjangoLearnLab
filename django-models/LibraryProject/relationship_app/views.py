from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library   # ✅ Import both models

def list_books(request):
    books = Book.objects.all()   # ✅ use objects
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
