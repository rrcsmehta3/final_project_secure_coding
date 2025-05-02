"""
Description: Module 3- Logic and Loops
Author: Sapana Mehta
Date: 7-02-2024
"""
from pprint import pprint
import csv

# Define an empty dictionary to store account balances
account_balances = {}
file_path = "account_balances.txt"

# Open the input file and read its contents
with open(file_path, "r") as input_file:
    # Process each line in the file
    for line in input_file:
        # Split each line based on the pipe delimiter
        account_number, balance = line.strip().split("|")

        # Convert balance to float
        balance = float(balance)

        # Add the account number and balance to the dictionary
        account_balances[account_number] = balance

# Use pretty print module to display the contents of the dictionary

pprint(account_balances)

# Calculatation of interest
def calculate_interest(balance):
    if balance > 0:
        if balance < 1000:
            rate = 0.01
        elif balance < 5000 and balance >= 1000:
            rate = 0.25
        elif balance >= 5000:
            rate = 0.05
    else:
        rate = 0.1
    return balance + ((balance * rate) / 12)
    
# Iterate through the dictionary of bank records and update balances
for account_number, balance in account_balances.items():
    updated_balance = calculate_interest(balance)
    account_balances[account_number] = updated_balance

# Display the updated contents of the dictionary using the pprint module
pprint(account_balances)

# Define the filename based on the first and last initials
filename = "updated_balances_FL.csv"

# Define the headings for the file
fieldnames = ['Account', 'Balance']

# Open the CSV file in write mode using a context manager
with open(filename, 'w', newline='') as csvfile:
    
    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header row with column names
    writer.writeheader()
    
    # Iterate through the dictionary of updated account balances and write each record to the CSV file
    for account_number, balance in account_balances.items():
        writer.writerow({'Account': account_number, 'Balance': balance})

# Verify the data has been successfully written to the file
print(f"Data has been successfully written to {filename}")

# Verify that the file does not contain any blank rows
with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    blank_rows = sum(1 for row in data if not any(row))
    if blank_rows > 0:
        print("The file contains blank rows.")
    else:
        print("No blank rows found in the file.")

# Declare  filename on the basis of  first and last initials
filename = "updated_balances_FL.csv"

# CSV file opening  in read mode using a context manager
with open(filename, 'r', newline='') as csvfile:
    # Creating a CSV reader object
    reader = csv.DictReader(csvfile)
    
    # Print the contents of the file to the console
    for row in reader:
        print(row)

# Verify the correct data displays
print(f"Updated data from {filename} displayed successfully.")