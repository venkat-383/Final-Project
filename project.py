import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View total expense")
        print("3. Filter by category")
        print("4. Exit")

        choice = input("Choose (1-4): ")

        if choice == "1":
            category = input("Category: ")
            description = input("Description: ")
            amount = float(input("Amount: "))
            date = datetime.now().strftime("%Y-%m-%d")

            expense = create_expense(date, category, description, amount)
            save_expense(expense)
            print("Expense added.")

        elif choice == "2":
            expenses = read_expenses()
            print(f"Total Expense: ₹{calculate_total(expenses)}")

        elif choice == "3":
            category = input("Enter category: ")
            expenses = read_expenses()
            filtered = filter_by_category(expenses, category)

            if not filtered:
                print("No expenses found.")
            else:
                for e in filtered:
                    print(e)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


# --------- TESTABLE FUNCTIONS (REQUIRED) ----------

def create_expense(date, category, description, amount):
    return {
        "date": date,
        "category": category,
        "description": description,
        "amount": float(amount)
    }


def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)


def filter_by_category(expenses, category):
    return [
        expense for expense in expenses
        if expense["category"].lower() == category.lower()
    ]


# --------- FILE HANDLING (HELPER FUNCTIONS) ---------

def save_expense(expense):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            expense["date"],
            expense["category"],
            expense["description"],
            expense["amount"]
        ])


def read_expenses():
    expenses = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append({
                    "date": row[0],
                    "category": row[1],
                    "description": row[2],
                    "amount": float(row[3])
                })
    except FileNotFoundError:
        pass

    return expenses


if __name__ == "__main__":
    main()

