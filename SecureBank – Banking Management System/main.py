"""
Main entry point of the Bank Management System.
Handles user menu interaction.
"""

from bank import Bank

bank = Bank()

MENU = """
1. Create Account
2. Deposit
3. Withdraw
4. Show Details
5. Delete Account
6. Exit
"""

while True:
    print(MENU)
    choice = input("Select an option: ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        bank.withdraw()
    elif choice == "4":
        bank.show_details()
    elif choice == "5":
        bank.delete_account()
    elif choice == "6":
        print("Thank you for using the system.")
        break
    else:
        print("Invalid option.")
