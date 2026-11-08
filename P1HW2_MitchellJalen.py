# Jalen Mitchell
# November 7, 2026
# P1HW2 - Travel Expenses
# This program calculates travel expenses and shows the remaining budget.

# Pseudocode:
# 1. Ask the user to enter their travel budget.
# 2. Ask the user where they are traveling.
# 3. Ask how much they plan to spend on gas, accommodation, and food.
# 4. Add the three expenses to get the total travel cost.
# 5. Subtract the total expenses from the starting budget.
# 6. Display the destination, budget, expenses, and remaining balance.

print("This program calculates and displays travel expenses")
print()

# Get the travel budget and destination from the user.
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")

# Get each planned travel expense from the user.
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Add all expenses together.
total_expenses = gas + accommodation + food

# Subtract the expenses from the original budget.
remaining_balance = budget - total_expenses

# Display the travel budget and expense summary.
print()
print("-----------------Travel Expenses-----------------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print()
print("Fuel: ${:.2f}".format(gas))
print("Accommodation: ${:.2f}".format(accommodation))
print("Food: ${:.2f}".format(food))
print()
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")
