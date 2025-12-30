# Expense Tracker

#### Video Demo: https://youtu.be/I0BR7wi7rAg?si=Fax4n_tNvmKlPMPo

## Description

Expense Tracker is a command-line based Python application developed as my final project for Harvard’s CS50P: Introduction to Programming with Python. The purpose of this project is to provide a simple yet practical tool that allows users to record, analyze, and manage their daily expenses while demonstrating core Python programming concepts taught throughout the course.

The program enables users to add expenses with details such as date, category, description, and amount. Users can then view the total amount spent or filter expenses by a specific category. All data is stored persistently using a CSV file so that expenses are not lost when the program exits. This makes the application useful beyond a single runtime and closer to a real-world utility.

This project was intentionally designed to go beyond the complexity of individual problem sets by combining multiple concepts including loops, conditionals, functions, file handling, and automated testing.

## Design and Implementation

A key design decision in this project was to separate user interaction from core logic. The `main()` function is responsible only for handling user input and displaying output. Core functionality such as creating an expense, calculating the total expense, and filtering expenses by category is implemented in separate top-level functions.

This separation was necessary to make the program testable using pytest, as testing functions that rely directly on user input or printed output is difficult. By designing pure functions that accept parameters and return values, I was able to write reliable automated tests while keeping the application logic clean and maintainable.

Another design choice was the use of a CSV file instead of a database. CSV files are lightweight, human-readable, and sufficient for the scale of this project. They also align well with the file I/O concepts taught in CS50P.

## Files Included

- `project.py`:
  This is the main application file. It contains the `main()` function along with all custom functions required for the program. The file defines functions for creating expense records, calculating total expenses, filtering expenses by category, saving expenses to a CSV file, and reading expenses from the file.

- `test_project.py`:
  This file contains automated tests written using pytest. It tests three core functions from `project.py`: creating an expense, calculating the total expense, and filtering expenses by category. These tests ensure the correctness of the program’s logic and demonstrate proper testing practices.

- `expenses.csv`:
  This file stores all recorded expense data. Each row represents a single expense and includes the date, category, description, and amount. The file is created automatically if it does not already exist.

- `requirements.txt`:
  This file lists external pip-installable dependencies required by the project. In this case, it includes pytest, which is used to execute automated tests.

## Testing

Testing was an important part of this project. By running pytest, the correctness of the core logic functions can be verified automatically. This helped ensure that changes to the code did not break existing functionality and reinforced good software development practices.

## Conclusion

This project demonstrates my understanding of Python fundamentals, modular program design, file handling, and automated testing. It reflects the skills developed throughout CS50P and represents a complete, well-structured Python application that meets all course requirements.

