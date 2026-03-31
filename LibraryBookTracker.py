import json
import os

FILE_NAME = "books.json"

# Load books from file
def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save books to file
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

# Add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    
    books = load_books()
    
    book = {
        "title": title,
        "author": author,
        "available": True
    }
    
    books.append(book)
    save_books(books)
    
    print("✅ Book added successfully!")

# View all books
def view_books():
    books = load_books()
    
    if not books:
        print("📭 No books available.")
        return
    
    print("\n📚 Book List:")
    for i, book in enumerate(books, 1):
        status = "Available" if book["available"] else "Borrowed"
        print(f"{i}. {book['title']} by {book['author']} [{status}]")

# Search book
def search_book():
    keyword = input("Enter book title to search: ").lower()
    books = load_books()
    
    found = False
    
    for book in books:
        if keyword in book["title"].lower():
            status = "Available" if book["available"] else "Borrowed"
            print(f"📖 {book['title']} by {book['author']} [{status}]")
            found = True
    
    if not found:
        print("❌ Book not found.")

# Borrow book
def borrow_book():
    title = input("Enter book title to borrow: ").lower()
    books = load_books()
    
    for book in books:
        if book["title"].lower() == title:
            if book["available"]:
                book["available"] = False
                save_books(books)
                print("📕 Book borrowed successfully!")
            else:
                print("⚠️ Book already borrowed.")
            return
    
    print("❌ Book not found.")

# Return book
def return_book():
    title = input("Enter book title to return: ").lower()
    books = load_books()
    
    for book in books:
        if book["title"].lower() == title:
            if not book["available"]:
                book["available"] = True
                save_books(books)
                print("📗 Book returned successfully!")
            else:
                print("⚠️ Book was not borrowed.")
            return
    
    print("❌ Book not found.")

# Delete book
def delete_book():
    title = input("Enter book title to delete: ").lower()
    books = load_books()
    
    for book in books:
        if book["title"].lower() == title:
            books.remove(book)
            save_books(books)
            print("🗑️ Book deleted successfully!")
            return
    
    print("❌ Book not found.")

# Main menu
def main():
    while True:
        print("\n====== 📚 Library Book Tracker ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()