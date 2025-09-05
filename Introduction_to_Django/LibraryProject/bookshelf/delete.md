# Delete Operation

```python
book.delete()
Book.objects.all()

# Expected Output:
# (1, {'bookshelf.Book': 1})
# <QuerySet []>
# Delete Operation

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()
Book.objects.all()

# Expected Output:
# (1, {'bookshelf.Book': 1})
# <QuerySet []>
