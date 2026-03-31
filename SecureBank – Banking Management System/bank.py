"""
Bank Management System
----------------------
A secure console-based banking system built using Python OOP principles.

Features:
- Account creation with validation
- Secure PIN hashing using SHA-256
- Deposit & Withdrawal operations
- Transaction history tracking
- Persistent storage using JSON
"""

import json
import random
import string
import hashlib
from pathlib import Path
from datetime import datetime


class Bank:
    """
    Bank class handles all banking operations and manages data persistence.
    """

    # Path to the JSON file used as a lightweight database
    DATABASE = Path("data.json")

    def __init__(self):
        """
        Constructor loads existing user data when the program starts.
        """
        self.data = self._load_data()

    # ==========================================================
    # Internal Utility Methods (Private Methods)
    # ==========================================================

    def _load_data(self):
        """
        Loads user data from JSON file.
        If file does not exist or is corrupted, returns empty list.
        """
        if self.DATABASE.exists():
            try:
                with open(self.DATABASE, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def _save_data(self):
        """
        Saves current state of data into JSON file.
        Ensures persistent storage.
        """
        with open(self.DATABASE, "w") as f:
            json.dump(self.data, f, indent=4)

    @staticmethod
    def _hash_pin(pin: int) -> str:
        """
        Hashes PIN using SHA-256 for security.
        Raw PINs are never stored in the database.
        """
        return hashlib.sha256(str(pin).encode()).hexdigest()

    def _generate_account_number(self):
        """
        Generates a unique 8-character alphanumeric account number.
        Ensures no duplicate account numbers exist.
        """
        while True:
            acc = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if not any(user["account_no"] == acc for user in self.data):
                return acc

    def _find_user(self, account_no, pin):
        """
        Finds and returns a user dictionary based on account number and PIN.
        Returns None if no matching user found.
        """
        hashed_pin = self._hash_pin(pin)
        for user in self.data:
            if user["account_no"] == account_no and user["pin"] == hashed_pin:
                return user
        return None

    # ==========================================================
    # Public Banking Operations
    # ==========================================================

    def create_account(self):
        """
        Creates a new bank account after validating user input.
        """
        try:
            name = input("Enter your name: ").strip()
            age = int(input("Enter your age: "))
            email = input("Enter your email: ").strip()
            pin = int(input("Enter 4-digit PIN: "))
        except ValueError:
            print("Invalid input. Please enter correct data types.")
            return

        # Basic validation checks
        if age < 18 or len(str(pin)) != 4:
            print("Account creation failed. Age must be 18+ and PIN must be 4 digits.")
            return

        account_no = self._generate_account_number()

        new_user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": self._hash_pin(pin),
            "account_no": account_no,
            "balance": 0,
            "transactions": []
        }

        self.data.append(new_user)
        self._save_data()

        print("\nAccount created successfully!")
        print(f"Your Account Number: {account_no}")

    def deposit(self):
        """
        Deposits money into an existing account.
        Records transaction history.
        """
        try:
            acc = input("Enter account number: ")
            pin = int(input("Enter PIN: "))
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Invalid input.")
            return

        if amount <= 0:
            print("Amount must be positive.")
            return

        user = self._find_user(acc, pin)

        if not user:
            print("Invalid account details.")
            return

        user["balance"] += amount

        # Record transaction
        user["transactions"].append({
            "type": "deposit",
            "amount": amount,
            "date": str(datetime.now())
        })

        self._save_data()
        print("Deposit successful.")

    def withdraw(self):
        """
        Withdraws money if sufficient balance exists.
        """
        try:
            acc = input("Enter account number: ")
            pin = int(input("Enter PIN: "))
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Invalid input.")
            return

        user = self._find_user(acc, pin)

        if not user:
            print("Invalid account details.")
            return

        if amount <= 0 or amount > user["balance"]:
            print("Invalid withdrawal amount.")
            return

        user["balance"] -= amount

        # Record transaction
        user["transactions"].append({
            "type": "withdraw",
            "amount": amount,
            "date": str(datetime.now())
        })

        self._save_data()
        print("Withdrawal successful.")

    def show_details(self):
        """
        Displays account details along with recent transactions.
        """
        try:
            acc = input("Enter account number: ")
            pin = int(input("Enter PIN: "))
        except ValueError:
            print("Invalid input.")
            return

        user = self._find_user(acc, pin)

        if not user:
            print("Invalid account details.")
            return

        print("\n--- Account Details ---")
        print(f"Name: {user['name']}")
        print(f"Age: {user['age']}")
        print(f"Email: {user['email']}")
        print(f"Balance: {user['balance']}")
        print("\nRecent Transactions:")

        for t in user["transactions"][-5:]:
            print(f"{t['type']} | {t['amount']} | {t['date']}")

    def delete_account(self):
        """
        Deletes a user account after confirmation.
        """
        try:
            acc = input("Enter account number: ")
            pin = int(input("Enter PIN: "))
        except ValueError:
            print("Invalid input.")
            return

        user = self._find_user(acc, pin)

        if not user:
            print("Invalid account details.")
            return

        confirm = input("Are you sure you want to delete this account? (y/n): ").lower()

        if confirm == "y":
            self.data.remove(user)
            self._save_data()
            print("Account deleted successfully.")
        else:
            print("Deletion cancelled.")
