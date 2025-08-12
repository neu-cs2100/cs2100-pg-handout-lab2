
class BankAccount:
    pass
    # Constructor: __init__(self, holder, number)
    # Attributes: account_holder (str), account_number (str), # balance (float, starts at 0.0)
    # Methods:
    #   deposit(self, amount) - adds money to balance (must be positive)
    #   withdraw(self, amount) - subtracts money from balance (cannot overdraw)
    #   get_balance() - returns current balance
    #   __str__(self) - returns formatted account information
    #
    # Handle invalid operations (negative deposits, overdrawing, etc.)



# Example output:

# Enter account holder name: Stu
# Enter account number: ACC001
# Account created successfully!

# Account Information:
# Account Holder: Stu
# Account Number: ACC001
# Current Balance: $0.00

# Enter deposit amount: 1000
# Successfully deposited $1000.00
# Current Balance: $1000.00

# Enter withdrawal amount: 250
# Successfully withdrew $250.00
# Current Balance: $750.00

# Enter withdrawal amount: 1000
# Error: Insufficient funds. Current balance: $750.00
