budget = 1000
print(f"Total budget before expenses: {budget}")

rent = 500
groceries = 250
transportation = 120
remain_budget_after_rent = budget - rent
remain_budget_after_groceries = budget - groceries
remain_budget_after_transportation = budget - transportation

total_remaining_budget = budget - rent - groceries - transportation

print(f"Remaining budget after rent expenses: {remain_budget_after_rent}")
print(f"Remaining budget after grocery expenses: {remain_budget_after_groceries}")
print (f"Remaining budget after transportation expenses: {remain_budget_after_transportation}")
print (f"Total remaining budget: {total_remaining_budget}")

