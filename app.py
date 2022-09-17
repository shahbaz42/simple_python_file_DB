from audioop import add
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
    f_ob = open('Accounts.csv', 'a+', newline='')
    f_wr = csv.DictWriter(f_ob, fieldnames=account_schema )
    f_wr.writeheader()
    f_ob.close()
    f_ob = open('./Ledger.csv', 'a+', newline='')
    f_wr = csv.DictWriter(f_ob, fieldnames=ledger_schema)
    f_wr.writeheader()
    f_ob.close()
    
def create_account(account_no, name, address, phone_number, PAN, account_type, balance):
    """
        Function for creating a new account
    """
    f_ob = open('Accounts.csv', 'a+', newline='')
    f_wr = csv.DictWriter(f_ob, fieldnames=account_schema)
    f_wr.writerow({
        "account_no" : account_no,
        "name" : name,
        "address" : address,
        "phone_number" : phone_number,
        "PAN" : PAN,
        "account_type" : account_type,
        "balance" : balance
    })
    f_ob.close()

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

# test create account
main()