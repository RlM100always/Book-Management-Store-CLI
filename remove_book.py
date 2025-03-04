def remove_book(books):
    isbn = input("Enter ISBN of the book to remove: ")
    
    # Iterate and find the book to delete
    for book in books:
        if book["isbn"] == isbn:
            books.remove(book)
            print("\033[92mBook removed successfully.\033[0m")
            break
    else:
        print("\033[91mBook not found.\033[0m")
    
    return books

