task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unspecified priority"

if # daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = f"'{task}' is a {priority} priority task"

# Process priority using Match Case
match priority:
    case "high":
        reminder += " that requires your focus"
    case "medium":
        reminder += " that should be addressed soon"
    case "low":
        reminder += ". Consider completing it when you have free time"
    case _:
        reminder = f"'{task}' has an invalid priority. Please use high, medium, or low."
        print(reminder)
        exit()

# Check if task is time-bound using if statement
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    if priority != "low":  # Only add this if not already low priority message
        reminder += " today."
else:
    reminder = "Invalid time-bound input. Please use yes or no."
    
# Print the final reminder
print(f"Reminder: {reminder}")time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += ".'Finish project report' is a high priority task that requires immediate attention today!."

print(reminder)
