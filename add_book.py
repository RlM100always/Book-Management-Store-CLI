import book_model

from book_data import save_books
from datetime import date



def add_book(books):
    isbn = input("Enter ISBN or Book Id: ")
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    publisher = input("Enter publisher name : ")
    

    try:
        yearofpub = int(input("Enter publication year (YYYY): ").strip())
        if yearofpub < 1000 or yearofpub > date.today().year:
            raise ValueError("Please enter a valid 4-digit year within a valid range.")
    except ValueError:
            print("\033[91mInvalid year format. Please enter a valid year (1000 to Current)\033[0m")
            return
    try:
        price = float(input("Enter price: "))
        if price <= 0:
            raise ValueError("\033[94mPrice must be positive\033[0m")
    except ValueError as e:
        print(e)
        return

    try:
        quantity = int(input("Enter quantity in stock: "))
        if quantity < 0:
            raise ValueError("\033[94mQuantity must be a non-negative integer.\033[0m")
    except ValueError as e:
        print(e)
        return

    if isbn in books:
        print("\033[94mA book with this ISBN / Book Id already exists.\033[0m")
        return

    new_book = book_model.BookModel(isbn, title, genre,author, price, quantity,publisher,yearofpub)
    books.append(new_book.con_to_dict())
    save_books(books)

    print("\033[92mBook added successfully.\033[92m")