import csv
import os.path
from os import path
import time
import traceback

# Schema of Account table
account_schema = ["account_no", "name", "address", "phone_number", "PAN", "account_type", "balance"]

#Schema of Ledger
ledger_schema = ['account_1', 'account_2', 'amount']

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

def display_transaction_history(account_no):
    """
        Function for displaying transaction history
    """
    f_obj = open('Ledger.csv', 'r')
    f_reader = csv.DictReader(f_obj)
    print("\n")
    for record in f_reader:
        if record['account_1'] == account_no :
            print("Debited : ", record)
        elif record['account_2'] == account_no :
            print("Credited : ", record)
    f_obj.close()


def transaction(credit_account, debit_account, amount):
    """
        Function for making transactions
    """
    t0 = time.time()
    temp = []
    success = 0

    f_obj_account_1 = open('Accounts.csv', 'r')
    f_reader_1 = csv.DictReader(f_obj_account_1)

    f_obj_account_2 = open('Accounts.csv', 'r')
    f_reader_2 = csv.DictReader(f_obj_account_2)

    f_obj_ledger = open('Ledger.csv', 'a+', newline='')
    f_writer = csv.DictWriter(f_obj_ledger, fieldnames=ledger_schema)

    try :
        for s_record in f_reader_1:
            if s_record['account_no'] == debit_account and int(s_record['balance']) >= int(amount):
                for r_record in f_reader_2:
                    if r_record['account_no'] == credit_account:

                        s_record['balance'] = str(int(s_record['balance']) - int(amount))
                        temp.append(s_record)

                        r_record['balance'] = str(int(r_record['balance']) + int(amount))
                        temp.append(r_record)

                        f_writer.writerow({
                            'account_1' : debit_account,
                            'account_2' : credit_account,
                            'amount' : amount,
                        })
                        success = 1
                        break
        
        f_obj_account_1.seek(0)
        next(f_obj_account_1)
        for record in f_reader_1:
            if record['account_no'] != temp[0]['account_no'] and record['account_no'] != temp[1]['account_no']:
                temp.append(record)
    
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        print("Wrong input entered")

    f_obj_account_1.close()
    f_obj_account_2.close()
    f_obj_ledger.close()

    if success == 1:
        f_obj_account_1 = open('Accounts.csv', 'w+', newline="")
        f_writer = csv.DictWriter(f_obj_account_1, fieldnames=account_schema)
        f_writer.writeheader()

        for record in temp:
            f_writer.writerow(record)

        f_obj_account_1.close()
        print("Transaction successful")
    else:
        print("Transaction failed")

    t1 = time.time()
    print("Time taken for transaction : ", (t1-t0)*1000 , "ms")
    
def main():
    """
        main function starts from here.
    """

    end = 1
    print("===================================================================================")
    print("\nSchema of Accounts table :\n", account_schema)
    while end == 1:
        choice = int(input("\nFor adding a record to Account table Press 1\n" +
                           "For displaying all Transaction details Press 2\n" +
                           "For making a Fund Transfer Press 3\n"))

        if choice == 1:
            account_no = input("Enter Account number of the account holder : ")
            name = input("Enter Name of the account holder : ")
            address = input("Enter Address of the account holder : ")
            phone_no = input("Enter Phone_no of the account holder : ")
            pan = input("Enter PAN of the account holder : ")
            type = input("Enter A/C type : ")
            balance = input("Enter initial deposit amount ")

            create_account(account_no,name,address,phone_no,pan,type,balance)
            print('\nAccount added successfully')

        elif choice == 2:
            account = input('Enter your account number : ')
            display_transaction_history(account)

        elif choice == 3:
            debit_account = input('\nEnter your Account number : ')
            credit_account = input('\nEnter the Payee Account number : ')
            amount = input('\nEnter the amount to transfer : ')
            transaction(credit_account, debit_account, amount)

        else:
            print("\nIllegal input !!!")

        end = int(input("\nDo you want to continue ?, If Yes press 1 else press 0\n==>"))
        if end != 0 and end != 1:
            print("\nIllegal input !!!")
            exit()

# test create account
# create_account("1234", "Shahbaz", "Ballia", "7398358012", "1111111", "Saving", 10000)
# create_account("4321", "proxymoron", "Ballia", "7398358011", "222222", "Saving", 10000)
# transaction("12345","54321",20)

main()
