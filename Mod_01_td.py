# A To Do List app that allows users to add, view, and delete tasks
# Project: Mod 1/w2 - To Do List

# Welcome Splash Screen
print("\n" + ("-" * 40) + "\n") # I'm all about the visual spacing

print('\nWelcome to "MY TO DO LIST"\n\n'
      'An interactive task tracking app\ndesigned by Jen Planque\n')

print("\n" + ("-" * 40))

# Get user's name upfront to address them throughout the app
username = input("What is your name? ").strip().title() # Capitalize & remove extra spaces
print("\n" + ("-" * 40) + "\n")
print(f"\nHello, {username}!\n")

# Initialize an empty list to store the global 'tasks' value
tasks = []

# I will be utilizing the following items to improve the app's ease of use:
'''
- Use of functions (def()) throughout to better organize the code
- Include try/except blocks to handle invalid inputs
- Allow user to loop back to start of main menu after each action, except Quit
'''

# Definition to add a new task to the master list
def add_task():
    try:
        task = input("Enter new task: \n").strip()
        if task == "":
            print("Cannot add blank task\n")
        else:
            tasks.append(task)
            print(f'Task: "{task}" added successfully!')
    except ValueError:
        print("Error: Invalid input. Please enter a valid task.")

# Definition to view all tasks in the master list
def view_tasks():
    print(f"\n{username}'s TASK LIST\n")
    if not tasks:
        print(
            "\nTask List is Empty\n"
            "Returning to Main Menu...\n"
            )
    else:
        try:
            i = 1
            for task in tasks:
                print(f"{i} - {task}")
                i += 1
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

# Definition to delete a task from the master list
def delete_tasks():
    if not tasks:
        print(
            "\nTask List is Empty\n"
            "Returning to Main Menu...\n"
        )
    else:
        try:
            print("Choose task to delete: \n")
            i  = 1
            for task in tasks:
                print(f"{i} - {task}")
                i += 1
            task_number = int(input("Enter task number to delete: \n"))
            if task_number in range(1, len(tasks) + 1):
                removed_task = tasks.pop(task_number - 1)
                print(f'Task "{removed_task}" deleted successfully!')
            else:
                print("Error: Task number not in range.")
        except ValueError:
            print("Error: Invalid entry - Please enter a valid number.")

# Definition for main menu options
def main_menu():
    tasks = []
    while True:
        try:
            print(
                "\n" + ("-" * 40) + "\n"
                "\n🔹 MAIN MENU 🔹\n"
                )
            selection = int(input("Please choose from the following options: \n\n"
                "1 - Add Task\n"
                "2 - View Tasks\n"
                "3 - Delete Task\n"
                "4 - Quit\n\n"
                "Selection: "
                ))
            if selection == 1:
                add_task()
            elif selection == 2:
                view_tasks()
            elif selection == 3:
                delete_tasks()
            elif selection == 4: # Exit the app
                print("\nGoodbye! 🙂\n")
                exit()
            else:
                print("\nInvalid selection: must choose a number between 1 and 4.\n")
        except ValueError:
            print("\nInvalid selection: must choose a number between 1 and 4.\n")

# Call the main menu function to start the app; this is the entry point
main_menu()