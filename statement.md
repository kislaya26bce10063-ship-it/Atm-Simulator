# Project Statement

## Project Title

ATM Simulator

## Problem Statement

Traditional ATM systems allow users to perform basic banking operations such as 
checking their balance, withdrawing money, and depositing money.

The purpose of this project is to develop a simple ATM Simulator using Python. 
The program provides a menu-driven interface where the user can log in using a PIN 
and perform basic banking transactions.

The project also validates user input, checks the available balance before 
withdrawal, and updates the balance after deposits and withdrawals.

## Scope of the Project

The scope of this project is limited to simulating basic ATM operations.

The project includes:

- PIN verification
- Balance checking
- Money withdrawal
- Money deposit
- Balance updating
- Input validation
- Menu-based interaction

The project is intended for educational purposes and does not connect to a real 
bank account or banking system.

## Target Users

The target users of this project are:

- Beginner Python students
- First-year college students
- Students learning programming fundamentals
- Users who want to understand how a simple ATM system works

## High-Level Features

### 1. PIN Verification

The program asks the user to enter a PIN. Access to the ATM menu is provided only 
when the correct PIN is entered.

### 2. Check Balance

The user can select the balance option to view the current account balance.

### 3. Withdraw Money

The user can enter an amount to withdraw. The program checks whether:

- The amount is greater than zero.
- The amount does not exceed the available balance.

If the conditions are valid, the amount is deducted from the balance.

### 4. Deposit Money

The user can enter an amount to deposit. The program checks that the amount is 
greater than zero and then adds it to the current balance.

### 5. Input Validation

The program handles invalid amounts and invalid menu choices by displaying suitable 
messages.

### 6. Exit

The user can select the exit option to end the ATM session.

## Limitations

- The PIN is fixed in the program.
- The balance is stored only while the program is running.
- There is no real bank account connection.
- There is no database.
- Only one user/account is supported.
- The program does not store transaction history.

## Future Improvements

The project can be improved by adding:

- Multiple user accounts
- Database connectivity
- Transaction history
- PIN change facility
- Receipt generation
- Multiple ATM users
- Daily withdrawal limits
- Better security features
