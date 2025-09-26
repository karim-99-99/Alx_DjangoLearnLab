from django.urls import path
from .views import BookListView, BookDetailView, UpdateView, DeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/', UpdateView.as_view(), name='book-update'),
    path('books/delete/', DeleteView.as_view(), name='book-delete'),
]
