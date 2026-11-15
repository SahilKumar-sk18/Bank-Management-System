# Bank-Management-System

About the Project : 
The Banking Management System is a simple, menu-driven Python project that simulates basic banking operations. It allows users to create bank accounts, deposit money, withdraw money, view account details, update personal information, and delete their accounts.

This project uses Python's Object-Oriented Programming (OOP) concepts and stores account information in a JSON file, making it easy to save and retrieve data without using a database server.

It is a beginner-friendly project designed to improve understanding of Python programming, file handling, JSON operations, classes, methods, and data management.

✨ Features
The application provides the following functionalities:

Create an Account : 
Register a new bank account.
Enter name, age, email, and a 4-digit PIN.
Automatically generate a unique account number.
Account creation is restricted to users aged 18 or above.

Deposit Money :
Deposit money into an existing account.
Verify the account number and PIN.
Deposit amounts must be greater than ₹0 and cannot exceed ₹10,000 per transaction.
Automatically update the account balance.

Withdraw Money :
Withdraw money from an existing account.
Verify account credentials.
Prevent withdrawals exceeding the available balance.
Display the remaining balance after a successful withdrawal.

View Account Details:
Retrieve account information using the account number and PIN.
Display personal details and account balance.
Hide the PIN when displaying account information.

Update Account Details :
Update the account holder's name.
Update the registered email address.
Change the account PIN.
Age, account number, and balance cannot be modified through this feature.


Delete an Account :
Delete an existing bank account.
Verify account credentials before deletion.
Ask for confirmation before permanently removing account information.



🛠️ Technologies Used :
Python 3 – Core programming language.
JSON – Used for storing and retrieving account information.
Random Module – Generates random account numbers.
String Module – Provides letters and digits for account number generation.
Pathlib Module – Checks whether the JSON database file exists.
File Handling – Reads and writes account information.



🧠 Python Concepts Used :
This project demonstrates practical implementation of:

Classes and Objects
Object-Oriented Programming (OOP)
Static Methods
Encapsulation
Lists and Dictionaries
List Comprehensions
Conditional Statements
Exception Handling
File Handling
JSON Serialization and Deserialization
Random Number Generation
String Manipulation
User Input and Output




🔮 Future Improvements :
Some features that can be added in future versions:

Transaction history.
Multiple user login system.
Password/PIN encryption and secure authentication.
Minimum balance requirements.
Money transfer between accounts.
Database integration using SQLite or MySQL.
Graphical User Interface (GUI).
Improved input validation and error handling.
