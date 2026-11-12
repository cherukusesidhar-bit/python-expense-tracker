"""Expense Tracker using Python, CSV and JSON."""

import csv
import json
from pathlib import Path
from datetime import date

CSV_FILE = Path(__file__).with_name("expenses.csv")
JSON_FILE = Path(__file__).with_name("expenses.json")


def load_expenses():
    if JSON_FILE.exists():
        try:
            data = json.loads(JSON_FILE.read_text(encoding="utf-8"))
            return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read expenses.json. Starting with an empty list.")
    return []


def save_expenses():
    JSON_FILE.write_text(json.dumps(expenses, indent=4), encoding="utf-8")
    with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "note"])
        writer.writeheader()
        writer.writerows(expenses)


def add_expense():
    category = input("Category (e.g. Food, Travel, Shopping): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    note = input("Note (optional): ").strip()
    expenses.append({
        "date": date.today().isoformat(),
        "category": category.title(),
        "amount": round(amount, 2),
        "note": note
    })
    save_expenses()
    print("Expense added successfully!")


def show_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nDATE         CATEGORY        AMOUNT       NOTE")
    print("-" * 62)
    for item in expenses:
        print(f"{item['date']:<12} {item['category']:<15} ₹{item['amount']:<10.2f} {item['note']}")
    print("-" * 62)
    print(f"Total expenses: ₹{sum(item['amount'] for item in expenses):.2f}")


def show_category_summary():
    if not expenses:
        print("No expenses to summarize.")
        return

    totals = {}
    for item in expenses:
        totals[item["category"]] = totals.get(item["category"], 0) + item["amount"]

    print("\nEXPENSE SUMMARY BY CATEGORY")
    print("-" * 35)
    for category, amount in sorted(totals.items()):
        print(f"{category:<20} ₹{amount:.2f}")
    print("-" * 35)
    print(f"{'Grand Total':<20} ₹{sum(totals.values()):.2f}")


def main():
    while True:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Category-wise summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_category_summary()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


if __name__ == "__main__":
    expenses = load_expenses()
    main()
