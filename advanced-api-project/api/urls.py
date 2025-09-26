from django.urls import path
from .views import BookListView, BookDetailView, UpdateBookView, DeleteBookView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', UpdateBookView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', DeleteBookView.as_view(), name='book-delete'),
]
