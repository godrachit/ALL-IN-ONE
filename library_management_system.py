# #? library management system


#* This is a simple library management system that allows users to add books, show available books, borrow books, and return books. 
#* The system uses two lists: one for available books and another for issued books. Users can interact with the system through a menu-driven interface.


books = []
issued_books = []

def add_book():
    name = input("Enter the name of the book: ")
    books.append(name)                                        #! add the book to the list
    print(f"Book '{name}' added successfully!")
    
def show_book():
    if len(books)==0:
        print("No books available.")
    else:
        print("Books available:")
        for book in books:
            print(f"- {book}")
            
def borrow_book():
    name = input("Enter the book you wanr ro borrow")
    if name in books:
        issued_books.append(name)                             #! add the book to the issued books list
        books.remove(name)                                    #! remove the book from the available books list
        print(f"Book '{name}' issued successfully!")
    else:
        print(f"Book '{name}' is not available.")
        
def return_book():
    name = input("Enter the book you want to return: ")
    if name in issued_books:
        issued_books.remove(name)                              #! remove the book from the issued books list
        books.append(name)                                     #! add the book back to the available books list
        print(f"Book '{name}' returned successfully!")
    else:
        print(f"Book '{name}' was not issued.")
        
def library():
    
    print("\nWelcome to the Library Management System")
    print("1. Add Book")
    print("2. Show Available Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            show_book()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("\nExiting the system. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")
            
library()
