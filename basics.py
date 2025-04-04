# Integer variable representing age
age = 33  # Age is an integer value

# Float variable representing weight
weight = 92.5  # Weight is a float value with decimal precision

# String variable representing the name
name = "Mohit"  # Name is a string type representing a person's name

# Boolean variable indicating if the person is a gym lover
is_gym_lover = True  # True means the person loves gym workouts

# Output information about the person (name, age, weight)
print(name, "is", age, "years old and weighs", weight, "kg.")
print("Loves gym workouts:", is_gym_lover)  # Prints whether the person loves gym workouts

# Two integers for arithmetic operations
a = 10
b = 5

# Arithmetic Operators - performing basic mathematical operations
print("Addition:", a + b)  # Prints the result of adding a and b
print("Subtraction:", a - b)  # Prints the result of subtracting b from a
print("Multiplication:", a * b)  # Prints the result of multiplying a and b
print("Division:", a / b)  # Prints the result of dividing a by b

# Comparison Operators - checking relations between the two numbers
print("Is a greater than b?", a > b)  # Prints whether a is greater than b
print("Is a equal to b?", a == b)  # Prints whether a is equal to b

# Uncomment and use to check if a number entered by the user is positive, negative, or zero
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# Loop to print numbers from 1 to 5
for i in range(1, 6):
    print(i)  # Prints numbers from 1 to 5

# List representing workout days
workout_days = ["Monday", "Wednesday", "Friday"]

# Loop through each workout day and print
for day in workout_days:
    print("Workout scheduled on", day)  # Prints the workout day

# While loop to print numbers from 1 to 5
num = 1

while num <= 5:
    print(num)  # Prints the current value of num
    num += 1  # Increment num by 1 to avoid an infinite loop

# Function to greet a person with their name
def greet(name):
    print(f'Hello, {name}!')  # Prints a greeting message with the provided name

# Calling the greet function for two names
greet("Mohit")
greet("Sharma")

# Function to add two numbers
def add(a, b):
    return a + b  # Returns the sum of a and b

# Function to subtract two numbers
def subtract(a, b):
    return a - b  # Returns the difference between a and b

# Function to multiply two numbers
def multiply(a, b):
    return a * b  # Returns the product of a and b

# Function to divide two numbers (handling division by zero)
def divide(a, b):
    return a / b if b != 0 else "Error! Division by zero."  # Divides a by b if b is not zero, otherwise returns an error message

# Loop to implement a basic calculator with options for the user
while True:
    print("\nCalculator Menu:")  # Display the menu
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Modulus")
    print("7. Exit")

    # Get user's choice
    choice = input("Enter your choice (1-7): ").strip()  # Strips extra spaces or newlines from user input

    if choice == '7':
        print("Exiting... Goodbye!")  # Exit message when choice is 7
        break  # Exit the loop and end the program

    if choice not in ('1', '2', '3', '4', '5', '6', '7'):
        print("Invalid choice! Please try again.")  # Error message for invalid choice
        continue  # Restart the loop to ask for a valid choice

    # Get two numbers from the user for calculation
    num1 = float(input("Enter first number: "))  # First number
    num2 = float(input("Enter second number: "))  # Second number

    # Execute the appropriate operation based on the user's choice
    if choice == '1':
        print("Result:", add(num1, num2))  # Addition
    elif choice == '2':
        print("Result:", subtract(num1, num2))  # Subtraction
    elif choice == '3':
        print("Result:", multiply(num1, num2))  # Multiplication
    elif choice == '4':
        print("Result:", divide(num1, num2))  # Division
    elif choice == '5':
        print("Result:", num1 ** num2)  # Exponentiation (num1 raised to the power of num2)
    elif choice == '6':
        print("Result:", num1 % num2)  # Modulus (remainder of division)

# List of fruits
fruits = ["apple", "banana", "cherry"]

# Accessing and printing elements from the list
print(fruits[0])  # Accessing the first element (apple)
print(fruits[-1])  # Accessing the last element (cherry)
fruits.append("orange")  # Adding 'orange' to the end of the list
print(fruits)  # Printing the updated list after append
fruits.insert(1, "kiwi")  # Inserting 'kiwi' at index 1
print(fruits)  # Printing the updated list after insert
fruits.remove("banana")  # Removing 'banana' from the list
print(fruits)  # Printing the updated list after removal
fruits.sort()  # Sorting the list in alphabetical order
print(fruits)  # Printing the sorted list
fruits.reverse()  # Reversing the list
print(fruits)  # Printing the reversed list

# Creating a tuple for coordinates (immutable)
coordinates = (10, 20)

# Accessing elements of a tuple
print("X coordinate:", coordinates[0])  # Accessing the first element (X)
print("Y coordinate:", coordinates[1])  # Accessing the second element (Y)

# Tuples are immutable, so we cannot modify them
# Uncommenting the following line would result in an error:
# coordinates[0] = 50  # This will cause an error because tuples cannot be modified

# Creating a dictionary to store person details
person = {
    "name": "John Doe",  # Name of the person
    "age": 30,  # Age of the person
    "city": "New York"  # City of residence
}

# Accessing and printing values from the dictionary using keys
print(person["name"])  # Prints the name
print(person["age"])  # Prints the age

# Updating values in the dictionary
person["age"] = 31  # Updating the age
print(person["age"])  # Prints the updated age

# Updating the city of residence
person["city"] = "Los Angeles"  # Changing the city
print(person["city"])  # Prints the updated city

# Deleting a key-value pair from the dictionary
del person["city"]  # Removing the city entry
print(person)  # Printing the updated dictionary

# Iterating over the dictionary to print all key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")  # Prints each key and its corresponding value

# Mini Project: To-Do List Manager (File-based)
def show_task():
    """Function to display tasks from the file."""
    try:
        with open("tasks.txt", "r") as file:  # Open the tasks file in read mode
            tasks = file.readlines()  # Read all lines (tasks) from the file
            if not tasks:
                print("No tasks found.")  # Message if no tasks are present
            else:
                print("Tasks:")
                for task in tasks:
                    print(task.strip())  # Print each task after stripping whitespace
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")  # Error message if file not found

def add_task(task):
    """Function to add a task to the file."""
    with open("tasks.txt", "a") as file:  # Open the tasks file in append mode
        file.write(task + "\n")  # Write the task to the file

def add_task_deadline(task, deadline):
    """Function to add a task with a deadline to the file."""
    with open("tasks.txt", "a") as file:  # Open the tasks file in append mode
        file.write(f"{task} (Deadline: {deadline})\n")  # Write the task and deadline to the file

def remove_task(task):
    """Function to remove a task from the file."""
    try:
        with open("tasks.txt", "r") as file:  # Open the tasks file in read mode
            tasks = file.readlines()  # Read all lines (tasks) from the file
        with open("tasks.txt", "w") as file:  # Open the tasks file in write mode to overwrite
            for t in tasks:
                if t.strip() != task:  # Write back only the tasks that are not removed
                    file.write(t)
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")  # Error message if file not found
    except Exception as e:
        print(f"Error: {e}")
        # General error handling for any other exceptions
# Main loop for the To-Do List Manager
while True:
    print("\nTo-Do List Menu:")  # Display the menu
    print("1. Show Tasks")  # Option to show tasks
    print("2. Add Task")  # Option to add a task
    print("3. Remove Task")  # Option to remove a task
    print("4. Add Task Deadline")  # Option to clear all tasks
    print("5. Exit")  # Option to exit the program

    choice = input("Enter your choice (1-4): ").strip()  # Get user's choice
    if choice == '1':
        show_task()  # Show tasks if option 1 is chosen
    elif choice == '2':
        task = input("Enter the task to add: ").strip()  # Get the task to add
        add_task(task)  # Add the task to the file
        print(f"Task '{task}' added.")  # Confirmation message after adding the task
    elif choice == '3':
        task = input("Enter the task to remove: ").strip()  # Get the task to remove
        remove_task(task)  # Remove the task from the file
        print(f"Task '{task}' removed.")  # Confirmation message after removing the task
    elif choice == '4':
        task = input("Enter the task to add: ").strip()
        deadline = input("Enter the deadline (YYYY-MM-DD): ").strip()  # Get the task and deadline to add
        add_task_deadline(task, deadline)  # Add the task with deadline to the file
        print(f"Task '{task}' with deadline '{deadline}' added.")
    elif choice == '5':
        print("Exiting... Goodbye!")
        break  # Exit message when choice is 4
    else:
        print("Invalid choice! Please try again.")
        continue  # Restart the loop to ask for a valid choice