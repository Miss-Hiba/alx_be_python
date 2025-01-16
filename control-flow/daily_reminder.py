task = input("Enter your task: ") 
priority = input("Enter the task’s priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound (yes or no): ").lower()
match priority: 
    case 'high': 
        reminder = f"Your high priority task is: {task}"
    case 'medium': 
        reminder = f"Your medium priority task is: {task}" 
    case 'low': 
        reminder = f"Your low priority task is: {task}"
    case _: 
        reminder = "Invalid priority level."
if time_bound == 'yes': 
    reminder += " that requires immediate attention today!"
print("Reminder: " + reminder)
