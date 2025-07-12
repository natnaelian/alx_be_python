# finance_calculator.py

# Prompt user for input
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate projected annual savings with 5% interest
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Display the results
print(f"\nEnter your monthly income: {monthly_savings:.2f}.")
print(f"Enter your total monthly expenses: {projected_savings:.2f}.")
