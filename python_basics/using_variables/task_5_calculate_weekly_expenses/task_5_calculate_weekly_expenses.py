income = float(input("Enter your income: "))
weekly_expenses = float(input("Enter how much expenses you spent per week: "))

remaining_balance = round(income - weekly_expenses, 2)
print(f"Your remaining balance is: {remaining_balance}")