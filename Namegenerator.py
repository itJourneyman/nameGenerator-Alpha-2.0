import random
import time

# Lists of common first names and last names
first_names = ["John", "Jane", "Michael", "Emily", "David", "Sophia", "Robert", "Olivia", "William", "Ava", "Ella", "Daniel", "Emma", "Liam", "Mia"]
last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Harris", "Martin", "Garcia"]

# Function to generate a random name
def generate_random_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

def add_name(list, name):
    list.append(name)
    print(f"{name} has been added.")

def remove_name(list, name):
    if name in list:
        list.remove(name)
        print(f"{name} has been removed.")
    else:
        print(f"{name} is not in the list.")

while True:
    print("\nOptions:")
    print("1. Generate names")
    print("2. Adjust the number of names to generate")
    print("3. Add a first name")
    print("4. Add a last name")
    print("5. Remove a first name")
    print("6. Remove a last name")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num_names = int(input("Enter the number of names to generate: "))
        for _ in range(num_names):
            name = generate_random_name()
            print(name)
        time.sleep(1)

    elif choice == "2":
        num_names = int(input("Enter the new number of names to generate: "))

    elif choice == "3":
        first_name = input("Enter a first name to add: ")
        add_name(first_names, first_name)

    elif choice == "4":
        last_name = input("Enter a last name to add: ")
        add_name(last_names, last_name)

    elif choice == "5":
        first_name = input("Enter a first name to remove: ")
        remove_name(first_names, first_name)

    elif choice == "6":
        last_name = input("Enter a last name to remove: ")
        remove_name(last_names, last_name)

    elif choice == "7":
        break

    else:
        print("Invalid choice. Please select a valid option.")
