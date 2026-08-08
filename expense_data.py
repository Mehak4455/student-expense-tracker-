import json
import os

FILE_NAME = "expense_data.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return {
        "income": 0,
        "expenses": []
    }


def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


data = load_data()


def add_income():
    amount = float(input("Enter income amount: ₹"))
    data["income"] += amount
    save_data()
    print("✅ Income added successfully!\n")


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")

    data["expenses"].append({
        "name": name,
        "amount": amount,
        "category": category
    })

    save_data()
    print("✅ Expense added successfully!\n")


def show_expenses():
    if not data["expenses"]:
        print("No expenses added yet.\n")
        return

    print("\n--- All Expenses ---")

    for i, expense in enumerate(data["expenses"], 1):
        print(
            f"{i}. {expense['name']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']}"
        )

    print()


def show_summary():
    total_expenses = sum(
        expense["amount"] for expense in data["expenses"]
    )

    balance = data["income"] - total_expenses

    print("\n===== SUMMARY =====")
    print(f"💰 Total Income: ₹{data['income']:.2f}")
    print(f"💸 Total Expenses: ₹{total_expenses:.2f}")
    print(f"💵 Remaining Balance: ₹{balance:.2f}\n")


def category_summary():
    if not data["expenses"]:
        print("No expenses available.\n")
        return

    categories = {}

    for expense in data["expenses"]:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n===== CATEGORY-WISE EXPENSES =====")

    for category, amount in categories.items():
        print(f"📂 {category}: ₹{amount:.2f}")

    print()


while True:

    print("===== STUDENT EXPENSE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Expenses")
    print("4. Show Summary")
    print("5. Category-wise Summary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_income()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        show_expenses()

    elif choice == "4":
        show_summary()

    elif choice == "5":
        category_summary()

    elif choice == "6":
        print("Thank you for using Student Expense Tracker! 👋")
        break

    else:
        print("❌ Invalid choice. Please try again.\n")