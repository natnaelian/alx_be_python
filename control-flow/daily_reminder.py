# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case block for priority handling
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to address it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"\nNote: '{task}' is a medium priority task. Schedule it when convenient.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task but still needs attention today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority entered. Please use high, medium, or low.")
