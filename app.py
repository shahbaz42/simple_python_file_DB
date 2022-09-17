import csv
import os.path
from os import path

# Schema of Account table
account_schema = ["account_no", "name", "address", "phone_number", "PAN", "account_type", "balance"]

#Schema of Ledger
ledger_schema = ['account1', 'account_2', 'amount', "D/C"]

# code for opening/creating csv files
if not os.path.exists("./Accounts.csv") and not os.path.exists("./Ledger.csv"):
    # if DB files do not exist then create new empty files
    f_ob = open('Accounts.csv', 'a+')
    f_wr = csv.DictWriter(f_ob, fieldnames=account_schema )
    f_wr.writeheader()
    f_ob.close()
    f_ob = open('./Ledger.csv', 'a+')
    f_wr = csv.DictWriter(f_ob, fieldnames=ledger_schema)
    f_wr.writeheader()
    f_ob.close()
    
def create_account():
    """
        Function for creating a new account
    """
    pass

def display_transaction_history():
    """
        Function for displaying transaction history
    """
    pass

def transaction():
    """
        Function for making transactions
    """
    pass

def main():
    """
        main function starts from here.
    """

main()