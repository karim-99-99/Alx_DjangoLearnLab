from django.shortcuts import render
from django.http import HttpResponse
from .models import Book , Library
from django.views.generic import DetailView
# Create your views here.

def list_books(request):
    books = Book.objects.select_related("author").all()   # ✅ use objects
    output = "<h2>Books and their Authors</h2><ul>"
    for book in books:
        output += f"<li>{book.title} by {book.author.name}</li>"
    output += "</ul>"
    return HttpResponse(output)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
