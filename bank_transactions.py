"""
Description: Module 3- Logic and Loops
Author: Sapana Mehta 
Date: 7-02-2024
"""
# Import statements
import os
import random
from time import sleep

# Define transaction options
transaction_options = {"D", "W", "Q"}

# Declare a random bank balance
balance = float(random.randint(-1000, 10000))

while True:
    # Clean the screen 
    os.system('cls' if os.name == 'nt' else 'clear')

    # Displaying the interface print
    print("*" * 40)
    print("PIXELL RIVER FINANCIAL".center(40))
    print("ATM Simulator".center(40))
    print(f"Your current balance is: ${balance:,.2f}".center(40))
    print("Deposit: D".center(40))
    print("Withdraw: W".center(40))
    print("Quit: Q".center(40))
    print("*" * 40)

    # Promote the user for a selection
    selection = input("Enter your selection: ").upper()

    # Checking if the selection is valid
    if selection == "Q":
        # Quit the program
        print("Quit")
        break

    elif selection == "D":
        # Handle deposit
        amount = float(input("Enter amount of transaction: "))
        balance += amount
        # Display the updated balance
        print("*" * 40)
        print(f"  Your current balance is: ${balance:,.2f}".center(40))
        print("*" * 40)

    elif selection == "W":
        # Handle withdrawal
        amount = float(input("Enter amount of transaction: "))
        if amount > balance:
            print("*" * 40)
            print("INSUFFICIENT FUNDS".center(40))
            print("*" * 40)
        else:
            balance -= amount
            # Display the updated balance
            print("*" * 40)
            print(f"  Your current balance is: ${balance:,.2f}".center(40))
            print("*" * 40)

    else: 
        # Display invalid selection if the selection is made out of list 
        if selection not in transaction_options:
            print("*" * 40)
            print("INVALID SELECTION".center(40))
            print("*" * 40)

    # Pause of three seconds
    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
