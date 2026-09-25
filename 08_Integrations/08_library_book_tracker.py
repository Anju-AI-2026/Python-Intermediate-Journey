# Store library book information
books = [
    {
        "title": "Python Basics",
        "author": "John Smith",
        "price": 450,
        "available": True
    },
    {
        "title": "Data Science",
        "author": "Alice Brown",
        "price": 650,
        "available": False
    },
    {
        "title": "Machine Learning",
        "author": "David Lee",
        "price": 850,
        "available": True
    },
    {
        "title": "Web Development",
        "author": "Emma Wilson",
        "price": 550,
        "available": True
    },
    {
        "title": "Artificial Intelligence",
        "author": "Robert Green",
        "price": 900,
        "available": False
    }
]


# Transform book information
book_records = list(
    map(
        lambda book: {
            **book,
            "status": "Available" if book["available"] else "Borrowed"
        },
        books
    )
)


# Find available books
available_books = list(
    filter(
        lambda book: book["available"],
        book_records
    )
)


# Find borrowed books
borrowed_books = list(
    filter(
        lambda book: not book["available"],
        book_records
    )
)


# Find books priced above ₹600
expensive_books = list(
    filter(
        lambda book: book["price"] > 600,
        book_records
    )
)


# Calculate total value of all books
total_value = sum(
    book["price"]
    for book in book_records
)


# Find the most expensive book
most_expensive = max(
    book_records,
    key=lambda book: book["price"]
)


# Display all books
print("\n" + "=" * 60)
print("              📚 LIBRARY BOOK TRACKER")
print("=" * 60)

print("\n📋 ALL BOOKS")
print("-" * 60)

for book in book_records:
    print(
        f"{book['title']:<25} "
        f"{book['author']:<18} "
        f"₹{book['price']:<5} "
        f"{book['status']}"
    )


print("\n✅ AVAILABLE BOOKS")
print("-" * 60)

for book in available_books:
    print(f"{book['title']:<30} ₹{book['price']}")


print("\n📕 BORROWED BOOKS")
print("-" * 60)

for book in borrowed_books:
    print(f"{book['title']:<30} ₹{book['price']}")


print("\n💰 BOOKS PRICED ABOVE ₹600")
print("-" * 60)

for book in expensive_books:
    print(f"{book['title']:<30} ₹{book['price']}")


# Display summary
print("\n📊 LIBRARY SUMMARY")
print("-" * 60)
print(f"Total books           : {len(book_records)}")
print(f"Available books       : {len(available_books)}")
print(f"Borrowed books        : {len(borrowed_books)}")
print(f"Books above ₹600      : {len(expensive_books)}")
print(f"Total collection value: ₹{total_value}")
print(f"Most expensive book   : {most_expensive['title']}")
print(f"Highest book price    : ₹{most_expensive['price']}")
print("=" * 60)