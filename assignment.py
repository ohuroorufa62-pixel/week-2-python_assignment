# Python Week 2 Assignment
# This program calculates the total cost of items.

price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity you want: "))

total = price * quantity

print(f"{quantity} items at {price:.2f} each = {total:.2f}")