from rest_framework import generics, permissions , filters
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly 
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework" 
# ✅ List all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend , filters.SearchFilter , filters.OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    filterset_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
# ✅ Retrieve details of a single book
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ✅ Create a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # automatically set owner to current user
        serializer.save(owner=self.request.user)


# ✅ Update an existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]


# ✅ Delete a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]
