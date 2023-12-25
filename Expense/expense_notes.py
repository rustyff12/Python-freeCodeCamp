# Define a function to add an expense to the list of expenses
def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})


# Define a function to print all expenses in a user-friendly format
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


# Define a function to calculate the total expenses
def total_expenses(expenses):
    # Use the sum function and a lambda function to extract the "amount" from each expense dictionary
    return sum(map(lambda expense: expense["amount"], expenses))


# Define a function to filter expenses by category
def filter_expenses_by_category(expenses, category):
    # Use the filter function and a lambda function to filter expenses with the specified category
    return filter(lambda expense: expense["category"] == category, expenses)


# Define the main function to run the expense tracker program
def main():
    # Initialize an empty list to store expenses
    expenses = []

    # Run the program in a loop until the user chooses to exit
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Show total expenses")
        print("4. Filter expenses by category")
        print("5. Exit")

        # Take user input for the desired action
        choice = input("Enter your choice: ")

        # Handle user choices
        if choice == "1":
            # Prompt the user for amount and category, then add the expense
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(expenses, amount, category)

        elif choice == "2":
            # Display all expenses
            print("\nAll Expenses:")
            print_expenses(expenses)

        elif choice == "3":
            # Display the total expenses
            print("\nTotal Expenses: ", total_expenses(expenses))

        elif choice == "4":
            # Prompt the user for a category and display expenses for that category
            category = input("Enter category to filter: ")
            print(f"\nExpenses for {category}:")
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == "5":
            # Exit the program if the user chooses to do so
            print("Exiting the program.")
            break


# Run the main function if the script is executed
if __name__ == "__main__":
    main()
