import csv
import os

expenses = []

def add_expense():
    while True:
        try:
            item_name = input("Enter Item Name: ")
            category = input("Enter Category of Expense: ")
            vendor = input("Enter Purchase Vendor: ")
            order_number = input("Enter Order #: ")
            purchase_price = float(input("Enter Purchase Price: ").replace('$', ''))  # Remove '$' if present
            order_date = input("Enter Order Date: ")
            sold = input("Sold (yes or no): ")

            if sold.lower() == 'yes':
                sale_date = input("Enter Sale Date: ")
                sold_price = float(input("Enter Sold Price: ").replace('$', ''))  # Remove '$' if present
                profit = sold_price - purchase_price
            else:
                sale_date = ""
                sold_price = ""
                profit = ""

            expense = [item_name, category, vendor, order_number, purchase_price, order_date, sold, sale_date, sold_price, profit]
            expenses.append(expense)
            break
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the price.")

def export_to_csv():
    file_exists = os.path.isfile('expenses.csv')

    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Item Name", "Category", "Vendor", "Order #", "Purchase Price", "Order Date", "Sold", "Sale Date", "Sold Price", "Profit"])

        writer.writerows(expenses)

# Main loop
while True:
    action = input("Do you want to add an expense (yes/no)? ")

    if action.lower() == 'yes':
        add_expense()
    elif action.lower() == 'no':
        export_to_csv()
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
