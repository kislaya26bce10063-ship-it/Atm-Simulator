print("******************************")
print("         ATM SIMULATOR")
print("******************************")

pin = 1234
balance = 10000

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:

    print("\nLogin Successful!")

    while True:
        print("\n------ ATM MENU -------")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nYour balance is Rs.", balance)

        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Please enter a valid amount.")

            elif amount > balance:
                print("Insufficient balance.")

            else:
                balance = balance - amount
                print("Please collect your cash.")
                print("Remaining balance: Rs.", balance)

        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))

            if amount <= 0:
                print("Please enter a valid amount.")

            else:
                balance = balance + amount
                print("Money deposited successfully.")
                print("Updated balance: Rs.", balance)

        elif choice == 4:
            print("\nThank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("\nIncorrect PIN.")
    print("Transaction cancelled.")
