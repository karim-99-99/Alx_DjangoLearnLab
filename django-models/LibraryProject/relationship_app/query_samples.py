from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Create instances
    author = Author.objects.create(name="J.K. Rowling")
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author)
    library = Library.objects.create(name="City Library")
    library.books.add(book1, book2)
    librarian = Librarian.objects.create(name="Alice", library=library)

    # Query examples
    authors = Author.objects.all()
    books = Book.objects.select_related('author').all()
    libraries = Library.objects.prefetch_related('books').all()
    librarians = Librarian.objects.select_related('library').all()

    for lib in libraries:
        print(f"Library: {lib.name}, Books: {[book.title for book in lib.books.all()]}")

    for libn in librarians:
        print(f"Librarian: {libn.name}, Library: {libn.library.name}")