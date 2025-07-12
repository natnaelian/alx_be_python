# finance_calculator.py

# Prompt the user for financial inputs
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate annual savings and apply simple interest
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Output the results
print(f"\nYour monthly savings are ${monthly_savings:}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:}.")
