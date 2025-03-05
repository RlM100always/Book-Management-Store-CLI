import json
import os
from add_book import add_book
from view_books import view_books
from remove_book import remove_book
from book_data import load_books, save_books
from search_book import search_books

# Colors (ANSI escape codes)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear_console():
    """ Clear the console (works on Windows, macOS, Linux). """
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """ Display the main menu with colorful options. """
    clear_console()  
    print(f"{CYAN}╔══════════════════════════════════════════════════╗")
    print(f"║         📚 {YELLOW}Book Store Management System{CYAN} 📚       ║")
    print(f"╠══════════════════════════════════════════════════╣")
    print(f"║ {GREEN}1.{RESET} {MAGENTA}➕ Add Book{CYAN}                                   ║")
    print(f"║ {GREEN}2.{RESET} {MAGENTA}📖 View Books{CYAN}                                 ║")
    print(f"║ {GREEN}3.{RESET} {MAGENTA}❌ Remove Book{CYAN}                                ║")
    print(f"║ {GREEN}4.{RESET} {MAGENTA}🔍 Search Book{CYAN}                                ║")
    print(f"║ {GREEN}5.{RESET} {MAGENTA}🚪 Exit{CYAN}                                       ║")
    print(f"╚══════════════════════════════════════════════════╝{RESET}")
    choice = input(f"{YELLOW}👉 Enter your choice: {RESET}")
    return choice

def main():
    """ Main function to manage the bookstore system. """
    books = load_books()  # Load existing books from the data source
    print(f"{GREEN}📚 Book data loaded successfully!{RESET}")

    while True:
        user_choice = show_menu()

        if user_choice == '1':
            print(f"{GREEN}➕ You chose to Add a Book!{RESET}")
            add_book(books)  # Call the add_book function
            save_books(books)  # Save updated book list
            input(f"{YELLOW}👉 Press Enter to continue...{RESET}")

        elif user_choice == '2':
            print(f"{GREEN}📖 Viewing all Books...{RESET}")
            view_books(books)  # Call the view_books function
            input(f"{YELLOW}🔍 Press Enter to return to the menu...{RESET}")

        elif user_choice == '3':
            print(f"{GREEN}❌ Removing a Book...{RESET}")
            remove_book(books)  # Call the remove_book function
            save_books(books)  # Save after removing
            input(f"{YELLOW}👉 Press Enter to continue...{RESET}")

        elif user_choice == '5':
            print(f"{RED}🚪 Exiting the system. Goodbye!{RESET}")
            break
        elif user_choice == '4':
            search_books(books)
            input(f"{YELLOW}🔍 Press Enter to return to the menu...{RESET}")

        else:
            print(f"{RED}❗ Invalid choice. Please try again.{RESET}")
            input(f"{YELLOW}👉 Press Enter to return to the menu...{RESET}")

if __name__ == "__main__":
    main()
