from django.shortcuts import render
from django.http import HttpResponse
from .models import Book , Library

# Create your views here.

def list_books(request):
    books = Book.object.select_related('author').all()
    output = "<h2>Books and their Authors</h2><ul>"
    for book in books:
        output += f"<li>{book.title} by {book.author.name}</li>"
    output += "</ul>"
    return HttpResponse(output)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship/library_detail.html'
    context_object_name = 'library'
    