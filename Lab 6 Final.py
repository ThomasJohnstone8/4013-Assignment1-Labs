

# Define the days of the week and months of the year
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
monthsOfYear = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

# Dictionaries to hold tasks for each day of the week and each month of the year
tasksByDay = {day: [] for day in daysOfWeek} # The empty brackets will hold the tasks later
tasksByMonth = {month: [] for month in monthsOfYear}


# Function to display the main menu
def displayMenu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


# Main loop
def main():
    while True:
        displayMenu()
        action = input("Choose an action (1-4): ")

        if action == '1':  # Add task
            addTask()
        elif action == '2':  # View tasks
            viewTasks()
        elif action == '3':  # Delete task
            deleteTask()
        elif action == '4':  # Exit
            print("Closing the program.") # In the main function
            break
        else:
            print("Invalid option. Please choose a number (1-4).")


# Function to add a task to a day or month
def addTask():
    print("\nWhen do you want to add a task?")
    print("1. For a day of the week")
    print("2. For a month of the year")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':  # For a day of the week
        day = input(f"Enter the day of the week ({daysOfWeek}): ").capitalize()
        if day in tasksByDay: # Checks if the day is in the list
            task = input(f"Enter the task to add to {day}: ")
            tasksByDay[day].append(task) # Appends to the dictionary and adds the task
            print(f"Task added to {day}.")
        else:
            print("Invalid day entered.") # If not, it tells the user it is invalid and returns to add task page
            addTask()

    elif choice == '2':  # For a month of the year
        month = input(f"Enter the month of the year ({monthsOfYear}): ").capitalize()
        if month in tasksByMonth: # Checks if the month entered is in the list
            task = input(f"Enter the task to add to {month}: ")
            tasksByMonth[month].append(task) # Appends to the dictionary and adds the task
            print(f"Task added to {month}.")
        else:
            print("Invalid month entered.")
            addTask()
    else:
        print("Invalid choice. Please try again.")
        addTask()


# Function to view tasks for a day or month
def viewTasks():
    print("\nWhere do you want to view tasks?")
    print("1. For a day of the week")
    print("2. For a month of the year")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':  # For a day of the week
        day = input(f"Enter the day of the week ({daysOfWeek}): ").capitalize()
        if day in tasksByDay:
            if tasksByDay[day]:
                print(f"Tasks for {day}:")
                for i, task in enumerate(tasksByDay[day], 1):
                    print(f"{i}. {task}")
            else:
                print(f"No tasks found for {day}.")
        else:
            print("Invalid day entered.")
            viewTasks()


    elif choice == '2':  # For a month of the year
        month = input(f"Enter the month of the year ({monthsOfYear}): ").capitalize()
        if month in tasksByMonth:
            if tasksByMonth[month]:
                print(f"Tasks for {month}:")
                for i, task in enumerate(tasksByMonth[month], 1):
                    print(f"{i}. {task}")
            else:
                print(f"No tasks found for {month}.")
        else:
            print("Invalid month entered.")
            viewTasks()


# Function to delete a task from a day or month
def deleteTask():
    print("\nWhere do you want to delete a task?")
    print("1. From a day of the week")
    print("2. From a month of the year")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':  # For a day of the week
        day = input(f"Enter the day of the week ({daysOfWeek}): ").capitalize()
        if day in tasksByDay:
            if tasksByDay[day]:
                print(f"Tasks for {day}:")
                for i, task in enumerate(tasksByDay[day], 1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input(f"Enter the task number to delete (1-{len(tasksByDay[day])}): "))
                    if 1 <= task_num <= len(tasksByDay[day]):
                        deleted_task = tasksByDay[day].pop(task_num - 1)
                        print(f"Deleted task: {deleted_task}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Enter a number.")
            else:
                print(f"No tasks found for {day}.")
        else:
            print("Invalid day entered.")

    elif choice == '2':  # For a month of the year
        month = input(f"Enter the month of the year ({monthsOfYear}): ").capitalize()
        if month in tasksByMonth:
            if tasksByMonth[month]:
                print(f"Tasks for {month}:")
                for i, task in enumerate(tasksByMonth[month], 1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input(f"Enter the task number to delete (1-{len(tasksByMonth[month])}): "))
                    if 1 <= task_num <= len(tasksByMonth[month]):
                        deleted_task = tasksByMonth[month].pop(task_num - 1)
                        print(f"Deleted task: {deleted_task}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Enter a number.")
            else:
                print(f"No tasks found for {month}.")
        else:
            print("Invalid month entered.")

    else:
        print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    main()
