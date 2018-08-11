# Create 3 different user accounts
User.objects.create(first_name="jay",last_name="me", email="dank@gmail.com")
# Have the first user create/upload 2 books.
u1 = User.objects.first()
Book.objects.create(name="Dank", desc="best book", uploader = u1)
# Have the second user create/upload 2 other books.
u2 = User.objects.get(id= 2)
Book.objects.create(name="memes", desc="best book", uploader = u2)
# Have the third user create/upload 2 other books.
u3 = User.objects.get(id= 3)
Book.objects.create(name="dankmemes", desc="best book", uploader = u3)
# Have the first user like the last book and the first book
book1 = Book.objects.first()
book1.liked_users.add(u1)


# Have the second user like the first book and the third book
u2.liked_books.add(book1)
u2.liked_books.add(book3)
u2= User.objects.get(id=2)


# Have the third user like all books
u2= User.objects.get(id=3)
u3.liked_books.add(book1)
u3.liked_books.add(book2)
u3.liked_books.add(book3)
u3.liked_books.add(book4)
u3.liked_books.add(book5)
u3.liked_books.add(book6)
u3.liked_books.add(bookl)

# Display all users who like the first book
User.objects.filter(liked_books__id=1)

# Display the user who uploaded the first book
User.objects.filter(uploaded_books__id=1)
# Display all users who like the second book
User.objects.filter(liked_books__id=2)

# Display the user who uploaded the second book
User.objects.filter(uploaded_books__id=2)

