from project import create_expense, calculate_total, filter_by_category


def test_create_expense():
    expense = create_expense("2025-01-01", "Food", "Lunch", 150)
    assert expense["category"] == "Food"
    assert expense["amount"] == 150.0


def test_calculate_total():
    expenses = [
        {"amount": 100},
        {"amount": 200},
        {"amount": 50}
    ]
    assert calculate_total(expenses) == 350


def test_filter_by_category():
    expenses = [
        {"category": "Food", "amount": 100},
        {"category": "Travel", "amount": 200},
        {"category": "Food", "amount": 50}
    ]

    food_expenses = filter_by_category(expenses, "Food")
    assert len(food_expenses) == 2
