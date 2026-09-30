# ATM Simulator

## 1. Project Overview

The ATM Simulator is a simple Python project that performs basic ATM operations. It allows users to log in using a PIN and check their balance, withdraw money, deposit money, or exit the program.

This project is created to understand the basic concepts of Python programming.

## 2. Features

- PIN-based login
- Check account balance
- Withdraw money
- Deposit money
- Update balance after transactions
- Check for insufficient balance
- Validate the amount entered
- Exit the program

## 3. Technologies Used

- **Programming Language:** Python
- **IDE:** VS Code / IDLE
- **Platform:** GitHub

## 4. How to Install and Run

Follow these steps to run the project:

1. Install Python 3 on your computer.
2. Download or clone this GitHub repository.
3. Open the project folder in VS Code or any Python IDE.
4. Open the terminal.
5. Run the following command:

   ```bash
   python atm.py
   ```

6. Enter the PIN to access the ATM menu.

## 5. Login Details

For testing the program, use the following details:

- **PIN:** 1234
- **Initial Balance:** Rs. 10,000

## 6. How to Test the Project

1. Run the program and enter the correct PIN.
2. Select option 1 to check the balance.
3. Select option 2 to withdraw money.
4. Select option 3 to deposit money.
5. Select option 4 to exit the program.
6. Enter an amount greater than the available balance to test the insufficient balance condition.
7. Enter zero or a negative amount to test input validation.
8. Enter an incorrect PIN to test the login system.

## 7. Example Output

```text
******************************
         ATM SIMULATOR
******************************

Enter your PIN: 1234

Login Successful!

------ ATM MENU -------
1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit
```

## 8. Project Structure

```text
ATM-Simulator/
│
├── atm.py
├── README.md
└── statement.md
```

## 9. Limitations

- The PIN is fixed in the program.
- The initial balance is fixed.
- The balance is not saved after the program closes.
- The program does not use a database.
- It does not connect to a real bank account.

## 10. Future Improvements

- Add multiple user accounts.
- Connect the project to a database.
- Store transaction history.
- Allow users to change their PIN.
- Add daily withdrawal limits.

## 11. Conclusion

The ATM Simulator is a beginner-friendly Python project that demonstrates the use of variables, conditional statements, loops, and user input. It provides a simple simulation of basic ATM operations and helps develop programming and problem-solving skills.
