# 🏦 SecureBank Management System

A full-stack banking application built with Python that demonstrates secure data handling, OOP principles, and modern web interfaces using Streamlit.

LIVE DEMO - https://securebank-management-system-sldc9rsmhu9jearzdzsgyk.streamlit.app/

## 📌 Overview

SecureBank is a complete banking management system that showcases production-ready Python development practices. Built with both CLI and web interfaces, it handles real-world banking operations with security, data persistence, and error handling at its core.

**Why this project matters for Data Science:**
- Demonstrates data validation and cleaning techniques
- Shows persistent storage and state management
- Implements security best practices (hashing, validation)
- Uses OOP principles for scalable code architecture

## ✨ Features

### Core Banking Operations
- ✅ **Account Creation** - User registration with validation (18+ age check, 4-digit PIN requirement)
- 💰 **Deposit Money** - Add funds with transaction logging
- 💸 **Withdraw Money** - Secure withdrawals with balance verification
- 📊 **Transaction History** - Track last 5 transactions per account
- 🔐 **Secure Authentication** - SHA-256 PIN hashing (never stores plain text)
- 🗑️ **Account Deletion** - Remove accounts with confirmation

### Technical Highlights
- **Dual Interface**: Console-based CLI + Streamlit web app
- **Data Persistence**: JSON-based lightweight database
- **Security**: Cryptographic hashing, input validation, error handling
- **OOP Design**: Clean class structure with encapsulation
- **Unique Account Numbers**: 8-character alphanumeric generation with collision detection

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Web Framework**: Streamlit
- **Data Storage**: JSON
- **Security**: hashlib (SHA-256)
- **Standard Libraries**: json, pathlib, datetime, random, string

## 📂 Project Structure

```
securebank-management-system/
│
├── bank.py              # Core Bank class with all business logic
├── main.py              # Console-based CLI interface
├── app.py               # Streamlit web application
├── data.json            # Persistent user database
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

## 💻 Usage Examples

### Creating an Account
```python
# Via CLI
1. Select option 1 (Create Account)
2. Enter name, age, email
3. Set a 4-digit PIN
4. Receive unique account number

# Via Streamlit
1. Navigate to "Create Account" in sidebar
2. Fill in the form
3. Click "Create Account"
4. Account number displayed on success
```

### Making a Deposit
```python
# Authentication required: Account number + PIN
# Enter amount to deposit
# Transaction automatically logged with timestamp
```

### Viewing Account Details
```python
# Shows:
# - Name, age, email
# - Current balance
# - Last 5 transactions (type, amount, date)
```

## 🔒 Security Features

| Feature | Implementation |
|---------|----------------|
| **PIN Storage** | SHA-256 cryptographic hashing - raw PINs never stored |
| **Input Validation** | Age verification, PIN length check, positive amount enforcement |
| **Error Handling** | Try-except blocks prevent crashes from invalid inputs |
| **Account Numbers** | Unique 8-character alphanumeric codes with collision detection |
| **Data Integrity** | JSON validation on load, graceful handling of corrupted data |

## 🧠 Key Learning Outcomes

### Object-Oriented Programming
- Encapsulation with private methods (`_hash_pin`, `_find_user`)
- Separation of concerns (Bank logic vs UI)
- Class-based state management

### Data Handling
- JSON serialization and deserialization
- File I/O with pathlib
- Data validation and cleaning
- Transaction logging with timestamps

### Security
- Cryptographic hashing (never store plain text credentials)
- Multi-layer input validation
- Secure user authentication flow

### UI Development
- Streamlit components (forms, buttons, inputs)
- State management in Streamlit
- Error messaging and user feedback

## 🐛 Challenges Solved

### Challenge 1: Streamlit State Management
**Problem**: Streamlit reruns the entire script on every interaction, causing data reload issues and potential race conditions.

**Solution**: Implemented immediate `_save_data()` calls after every transaction and added exception handling in `_load_data()` to gracefully handle corrupted JSON during concurrent access.

### Challenge 2: Unique Account Number Generation
**Problem**: Random generation can produce duplicates, especially as the user base grows.

**Solution**: Created `_generate_account_number()` with a validation loop that checks against all existing accounts before returning a number.

### Challenge 3: Security vs Usability
**Problem**: Users want quick access; banks need security. Finding the right balance.

**Solution**: Multi-layer validation (age at creation, PIN format, amount positivity) + hashed credentials for all operations.


## 🤝 Contributing

This is a portfolio project, but suggestions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Vineet Prakash**


---

