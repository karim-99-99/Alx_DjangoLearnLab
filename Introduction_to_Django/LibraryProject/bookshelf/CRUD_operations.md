
---

✅ Do you want me to **generate all 4 `.md` files and one combined `CRUD_operations.md` for you now** so you can upload them to your `Alx_DjangoLearnLab/Introduction_to_Django` repo?

 Create Operation

```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output:
# <Book: 1984 by George Orwell>
yaml
Copy code

---

### ✅ **2. retrieve.md**
```markdown
# Retrieve Operation

```python
book = Book.objects.get(id=1)
book.title
book.author
book.publication_year

# Expected Output:
# '1984'
# 'George Orwell'
# 1949
yaml
Copy code

---

### ✅ **3. update.md**
```markdown
# Update Operation

```python
book.title = "Nineteen Eighty-Four"
book.save()
book.title

# Expected Output:
# 'Nineteen Eighty-Four'
yaml
Copy code

---

### ✅ **4. delete.md**
```markdown
# Delete Operation

```python
book.delete()
Book.objects.all()

# Expected Output:
# (1, {'bookshelf.Book': 1})
# <QuerySet []>
yaml
Copy code

---

### ✅ **5. CRUD_operations.md (Combined File)**
```markdown
# CRUD Operations in Django Shell

## Create
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output:
# <Book: 1984 by George Orwell>
Retrieve
python
Copy code
book = Book.objects.get(id=1)
book.title
book.author
book.publication_year

# Expected Output:
# '1984'
# 'George Orwell'
# 1949
Update
python
Copy code
book.title = "Nineteen Eighty-Four"
book.save()
book.title

# Expected Output:
# 'Nineteen Eighty-Four'
Delete
python
Copy code
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
