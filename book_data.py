import json
import os

def load_books() :
    try:
        file_path = os.path.abspath("books.json")
        print(file_path)
        with open(file_path) as file :
           return json.load(file)
    except FileNotFoundError:
        print("No data file found. Thats means currently book list is empty")
        return []

def save_books(books):
    file_path = os.path.abspath("books.json")
    with open(file_path, 'w') as file:
        json.dump(books, file, indent=4)
