# Box Constants
COLUMN_WIDTHS = [20, 20, 20, 10, 15, 10, 20, 20]  # Updated to match 8 columns
BOX_TOP = "─" * (sum(COLUMN_WIDTHS) + len(COLUMN_WIDTHS) + 1)
BOX_DIVIDER = "─" * (sum(COLUMN_WIDTHS) + len(COLUMN_WIDTHS) + 1)
BOX_BOTTOM = "─" * (sum(COLUMN_WIDTHS) + len(COLUMN_WIDTHS) + 1)
BOX_SIDE = "│"

# Function to print formatted rows with optional highlighting
def format_row(row, search_term=""):
    def highlight_text(text):
        if search_term and search_term.lower() in text.lower():
            start = text.lower().find(search_term.lower())
            end = start + len(search_term)
            highlighted = f"{text[:start]}\033[93m{text[start:end]}\033[0m{text[end:]}"
            # Calculate visible length without ANSI codes
            visible_length = len(text)
            return highlighted, visible_length
        return text, len(text)

    formatted_row = [highlight_text(str(item)) for item in row]
    return BOX_SIDE + "│".join(f" {text.ljust(width - (visible_length - len(text)) - 1)}" 
                                     for (text, visible_length), width in zip(formatted_row, COLUMN_WIDTHS)) + f" {BOX_SIDE}"

# Function to view and search books
def search_books(books):
    if not books:
        print("No books available.")
        return

    # Headers and column widths
    headers = ["ISBN No", "Title", "Author", "Price", "Genre", "Quantity", "Publisher", "Year of Publication"]

    # Search term input
    search_term = input("Enter search term: ").strip().lower()

    # Filter books by search term (case-insensitive)
    matching_books = [book for book in books if any(search_term in str(value).lower() for value in book.values())]

    if not matching_books:
        print("No matching books found.")
        return

    # Print header
    print(BOX_TOP)
    print(format_row(headers))
    print(BOX_DIVIDER)

    # Print rows for each matching book with highlighted search term
    for book in matching_books:
        print(format_row([
            book.get('isbn', 'N/A'),
            book.get('title', 'N/A'),
            book.get('author', 'N/A'),
            f"{book.get('price', 0):.2f}",
            book.get('genre', 'N/A'),
            book.get('quantity', 'N/A'),
            book.get('publisher', 'N/A'),
            book.get('year of publication', 'N/A'),
        ], search_term))
        print(BOX_DIVIDER)
