from datetime import datetime


# Data storage
library_books = {
    "Python": {"available": True},
    "Java": {"available": True},
    "C++": {"available": True}
}

issued_books = {}


# Fine calculation
def calculate_fine(days_late):
    fine = 0
    rate = 10

    week = 1
    while days_late > 0:
        days_in_week = min(7, days_late)
        fine += days_in_week * (rate * week)
        days_late -= 7
        week += 1

    return fine


# Show books
def show_books():
    print("\nAvailable Books:")
    for book, info in library_books.items():
        status = "Available" if info["available"] else "Issued"
        print(f"{book} - {status}")


# Issue book
def issue_book():
    name = input("Enter student name: ")
    book = input("Enter book name: ")

    if book in library_books and library_books[book]["available"]:
        days = int(input("Enter number of days: "))
        date = datetime.now()

        issued_books[book] = {
            "student": name,
            "days": days,
            "date": date
        }

        library_books[book]["available"] = False

        print("Book issued successfully.")
        print("Fine rule: After due date:")
        print("Week 1: Rs 10/day")
        print("Week 2: Rs 20/day")
        print("Week 3: Rs 60/day and so on")

    else:
        print("Book not available.")


# Return book
def return_book():
    book = input("Enter book name to return: ")

    if book in issued_books:
        record = issued_books[book]
        issue_date = record["date"]
        allowed_days = record["days"]

        actual_days = (datetime.now() - issue_date).days
        late_days = actual_days - allowed_days

        if late_days > 0:
            fine = calculate_fine(late_days)
            print(f"Late by {late_days} days")
            print(f"Fine: Rs {fine}")
        else:
            print("Returned on time")

        library_books[book]["available"] = True
        del issued_books[book]

    else:
        print("No such issued book.")


# Add book
def add_book():
    book = input("Enter new book name: ")

    if book in library_books:
        print("Book already exists.")
    else:
        library_books[book] = {"available": True}
        print("Book added successfully.")


# Remove book
def remove_book():
    book = input("Enter book name to remove: ")

    if book in library_books:
        if not library_books[book]["available"]:
            print("Cannot remove issued book.")
        else:
            del library_books[book]
            print("Book removed successfully.")
    else:
        print("Book not found.")


# View issued books
def view_issued_books():
    if not issued_books:
        print("No books issued.")
        return

    print("\nIssued Books Details:")
    print("-----------------------------")

    for book, record in issued_books.items():
        student = record["student"]
        issue_date = record["date"]
        allowed_days = record["days"]

        days_passed = (datetime.now() - issue_date).days
        remaining_days = allowed_days - days_passed

        print(f"Book: {book}")
        print(f"Student: {student}")
        print(f"Issued for: {allowed_days} days")

        if remaining_days > 0:
            print(f"Return in: {remaining_days} days")
        else:
            print(f"Overdue by: {abs(remaining_days)} days")

        print("-----------------------------")


# Main menu
def main():
    while True:
        print("\n----- LIBRARY MENU -----")
        print("1. Show Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Remove Book")
        print("6. View Issued Books")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_books()

        elif choice == "2":
            issue_book()

        elif choice == "3":
            return_book()

        elif choice == "4":
            add_book()

        elif choice == "5":
            remove_book()

        elif choice == "6":
            view_issued_books()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()