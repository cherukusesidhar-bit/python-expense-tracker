# Python Expense Tracker (CSV/JSON)

A command-line expense management application built with Python. It records daily expenses, saves them locally, and provides category-wise spending summaries.

## Features
- Add an expense with category, amount and optional note
- Automatically records the current date
- View all saved expenses
- Calculate total spending
- Display category-wise expense summaries
- Store records in both JSON and CSV formats
- Validate category and amount inputs

## Requirements
- Python 3.8 or later
- No external packages required

## Run
Open a terminal in this folder and execute:

```bash
python main.py
```

Choose an option from the menu. The application creates `expenses.json` and `expenses.csv` when the first expense is saved.

## Technologies Used
- Python
- CSV module
- JSON module
- datetime
- pathlib

## Author
Sesidhar
