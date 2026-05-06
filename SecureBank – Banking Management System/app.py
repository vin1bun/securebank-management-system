import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(page_title="Bank Management System", layout="centered")

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox("Menu", [
    "Create Account",
    "Deposit",
    "Withdraw",
    "Show Details",
    "Delete Account"
])

# -------------------------------
# CREATE ACCOUNT
# -------------------------------
if menu == "Create Account":
    st.header("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        if len(pin) != 4:
            st.error("PIN must be 4 digits")
        elif age < 18:
            st.error("Age must be 18+")
        else:
            account_no = bank._generate_account_number()

            new_user = {
                "name": name,
                "age": age,
                "email": email,
                "pin": bank._hash_pin(int(pin)),
                "account_no": account_no,
                "balance": 0,
                "transactions": []
            }

            bank.data.append(new_user)
            bank._save_data()

            st.success(f"Account Created! 🎉")
            st.info(f"Account Number: {account_no}")

# -------------------------------
# DEPOSIT
# -------------------------------
elif menu == "Deposit":
    st.header("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1.0)

    if st.button("Deposit"):
        user = bank._find_user(acc, int(pin)) if pin else None

        if user:
            user["balance"] += amount
            user["transactions"].append({
                "type": "deposit",
                "amount": amount,
                "date": str(__import__("datetime").datetime.now())
            })
            bank._save_data()
            st.success("Deposit successful 💰")
        else:
            st.error("Invalid details")

# -------------------------------
# WITHDRAW
# -------------------------------
elif menu == "Withdraw":
    st.header("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1.0)

    if st.button("Withdraw"):
        user = bank._find_user(acc, int(pin)) if pin else None

        if user:
            if amount > user["balance"]:
                st.error("Insufficient balance")
            else:
                user["balance"] -= amount
                user["transactions"].append({
                    "type": "withdraw",
                    "amount": amount,
                    "date": str(__import__("datetime").datetime.now())
                })
                bank._save_data()
                st.success("Withdrawal successful 💸")
        else:
            st.error("Invalid details")

# -------------------------------
# SHOW DETAILS
# -------------------------------
elif menu == "Show Details":
    st.header("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = bank._find_user(acc, int(pin)) if pin else None

        if user:
            st.subheader("User Info")
            st.write(f"Name: {user['name']}")
            st.write(f"Balance: ₹{user['balance']}")

            st.subheader("Recent Transactions")
            for t in user["transactions"][-5:]:
                st.write(t)
        else:
            st.error("Invalid details")

# -------------------------------
# DELETE ACCOUNT
# -------------------------------
elif menu == "Delete Account":
    st.header("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        user = bank._find_user(acc, int(pin)) if pin else None

        if user:
            bank.data.remove(user)
            bank._save_data()
            st.success("Account deleted ❌")
        else:
            st.error("Invalid details")

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey; font-size: 0.85rem;'>"
    "Created by <strong>Vineet Prakash</strong> · Data Scientist"
    "</div>",
    unsafe_allow_html=True
)
