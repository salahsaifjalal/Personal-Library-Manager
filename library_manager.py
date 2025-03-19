import json
import os
import pyttsx3


# File to store library data
LIBRARY_FILE = "library.txt"

# Initialize library as an empty list
library = []

# Function to load library from file
def load_library():
    global library
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            library = json.load(file)
        print("Library loaded successfully!")
    else:
        print("No existing library found. Starting with an empty library.")

# Function to save library to file
def save_library():
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file)
    print("Library saved successfully!")

# Function to add a book
def add_book():
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    library.append(book)
    print(f"Book '{title}' added successfully!")

# Function to remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]
    print(f"Book '{title}' removed successfully!")

# Function to search for a book
def search_book():
    search_term = input("Enter the title or author to search: ").lower()
    results = [book for book in library if search_term in book["title"].lower() or search_term in book["author"].lower()]

    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read_status'] else 'No'}")
    else:
        print("No matching books found.")

# Function to display all books
def display_all_books():
    if not library:
        print("The library is empty.")
    else:
        print("\nAll Books in Library:")
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read_status'] else 'No'}")

# Function to display statistics
def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("The library is empty.")
        return

    read_books = sum(book["read_status"] for book in library)
    percentage_read = (read_books / total_books) * 100

    print("\nLibrary Statistics:")
    print(f"Total Books: {total_books}")
    print(f"Percentage Read: {percentage_read:.3f}%")

# Main menu
def main_menu():
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        # Set properties
        engine.setProperty("rate", 120)  # Speed of speech (words per minute)

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("Exiting the program. Good bye!")
            # Speak the text
            engine.say(""" Thank you Sir Zia Khan. ya Allah, we ask you to give the respected legend 
                       Sir Ziaullah Khan great success in everything he does in this life, and to give him
                       the best place in the next life. Please bless his life with long years, 
                       lots of good things, and much happiness. Ameen. """)
            # Wait for the speech to finish
            engine.runAndWait()
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    load_library()
    main_menu()