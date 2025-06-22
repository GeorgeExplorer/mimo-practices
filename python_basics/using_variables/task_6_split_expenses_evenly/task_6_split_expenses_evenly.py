# get incomes per one person
income_person_one = float(input("Hi, you're the first person! Enter your income: "))
income_person_two = float(input("Hi, you're the second one! Enter your income: "))
income_person_three = float(input("Hello, you're the last one! Enter your income: "))

# calculate total income amount
total_income = int(income_person_one + income_person_two + income_person_three)

# get total expenses amount per week
total_weekly_expenses = int(float(input("Enter your total expenses per week: ")))

# calculate how much each person should pay
payment_per_person = int(total_weekly_expenses // 3)

# calculate how much expenses amount still remain to pay in total
remaining_expenses_amount = total_weekly_expenses % 3

# get total remaining balance
remaining_balance_after_paid_expenses = int(total_income - total_weekly_expenses)

# calculate remaining balance for each person
remaining_balance_person_one, remaining_balance_person_two, remaining_balance_person_three = int(income_person_one - payment_per_person), int(income_person_two - payment_per_person), int(income_person_three - payment_per_person)

print(f"Total income: {total_income}")

print(f"Total weekly expenses: {total_weekly_expenses}")

print(f"Each person should pay: {payment_per_person}")

print(f"Remaining expenses amount to pay: {remaining_expenses_amount}")

print(f"Total remaining balance of the income: {remaining_balance_after_paid_expenses}")

print(f"Person 1 remains: {remaining_balance_person_one}\nPerson 2 remains: {remaining_balance_person_two}\nPerson 3 remains: {remaining_balance_person_three}")
