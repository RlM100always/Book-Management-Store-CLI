# Box Constants
COLUMN_WIDTHS = [20, 20, 20, 10, 15, 10, 20, 20]  # Updated to match 8 columns
BOX_TOP = "─" * (sum(COLUMN_WIDTHS) + len(COLUMN_WIDTHS) + 1)
BOX_DIVIDER = "─" * (sum(COLUMN_WIDTHS) + len(COLUMN_WIDTHS) + 1)
BOX_BOTTOM = "─" * (sum(COLUMN_WIDTHS) + len(COLUMN_WIDTHS) + 1)
BOX_SIDE = "|"

# Function to print table
def view_books(books):
    if not books:
        print("No books available.")
        return
    
    # Headers and column widths
    headers = ["ISBN No", "Title", "Author", "Price", "Genre", "Quantity", "Publisher", "Year of Publication"]

    # Helper function to format rows
    def format_row(row):
        return BOX_SIDE + "│".join(f" {str(item).ljust(width - 1)}" for item, width in zip(row, COLUMN_WIDTHS)) + f" {BOX_SIDE}"

    # Print header
    print(BOX_TOP)
    print(format_row(headers))
    print(BOX_DIVIDER)

    # Print rows for each book
    for book in books:
        print(format_row([
            book.get('isbn', 'N/A'),
            book.get('title', 'N/A'),
            book.get('author', 'N/A'),
            f"{book.get('price', 0):.2f}",
            book.get('genre', 'N/A'),
            book.get('quantity', 'N/A'),
            book.get('publisher', 'N/A'),
            book.get('year of publication', 'N/A'),  # Ensure correct key matches your data
        ]))
        print(BOX_DIVIDER)




