import streamlit as st

# ------------------ CLASS DEFINITION ------------------
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number       # Public
        self._account_holder = account_holder      # Protected
        self.__balance = balance                   # Private

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ₹{amount}. New Balance: ₹{self.__balance}"
        else:
            return "Invalid deposit amount."

    # Public method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ₹{amount}. Remaining Balance: ₹{self.__balance}"
        else:
            return "Insufficient funds or invalid amount."

    # Getter for private balance
    def get_balance(self):
        return self.__balance

    # Protected method
    def _display_holder_info(self):
        return f"Account Holder: {self._account_holder}"

    # Private method
    def __apply_bank_charges(self):
        self.__balance -= 50
        return "₹50 bank charge applied."

    # Public method using private method internally
    def bankcharge(self):
        return self.__apply_bank_charges()

    def month_end_process(self):
        self.__apply_bank_charges()
        return "Month-end processing done. ₹50 charge applied."

    def quit(self):
        return "Thank you for banking with us!"


# ------------------ STREAMLIT UI ------------------
st.title("🏦 Indiana Bank Web Portal")

# Initialize account in session state
if "account" not in st.session_state:
    st.session_state.account = None

st.divider()
st.subheader("Create New Account")

# Account creation form
with st.form("create_account_form"):
    account_number = st.text_input("Enter Account Number")
    account_holder = st.text_input("Enter Account Holder Name")
    initial_balance = st.number_input("Initial Balance", min_value=0, step=100)
    create_account = st.form_submit_button("Create Account")

    if create_account:
        if not account_number or not account_holder.strip():
            st.warning("Please enter all details.")
        else:
            st.session_state.account = BankAccount(account_number, account_holder.strip(), initial_balance)
            st.success(f" Account created for {account_holder.strip()} with balance ₹{initial_balance}")

# Show account actions only if account exists
if st.session_state.account:
    st.divider()
    st.subheader("Account Operations")

    col1, col2, col3 = st.columns(3)

    with col1:
        deposit_amount = st.number_input("Deposit Amount", min_value=0, step=100, key="deposit_amount")
        if st.button("Deposit"):
            st.info(st.session_state.account.deposit(deposit_amount))

    with col2:
        withdraw_amount = st.number_input("Withdraw Amount", min_value=0, step=100, key="withdraw_amount")
        if st.button("Withdraw"):
            st.info(st.session_state.account.withdraw(withdraw_amount))

    with col3:
        if st.button("Apply Bank Charge"):
            st.info(st.session_state.account.bankcharge())

    # Month-end process
    if st.button("Run Month-End Process"):
        st.info(st.session_state.account.month_end_process())

    # Show current balance and holder info
    st.divider()
    st.subheader("Account Details")
    st.write(st.session_state.account._display_holder_info())
    st.write(f" **Current Balance:** ₹{st.session_state.account.get_balance()}")

    if st.button("Quit"):
        st.success(st.session_state.account.quit())
        st.session_state.account = None

else:
    st.info("No account yet. Please create one above.")
    
