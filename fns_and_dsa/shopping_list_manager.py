def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Error: Item name cannot be empty.")
        
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"Error: '{item}' not found in the shopping list.")
        
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("Shopping list is empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Error: Item name cannot be empty.")
        
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'
from datetime import datetime

def display_menu():
    """
    Displays the shopping list manager menu with the current date and time.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nShopping List Manager - {current_time}")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Error: Item name cannot be empty.")
        
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"Error: '{item}' not found in the shopping list.")
        
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("Shopping list is empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()from datetime import datetime

def display_menu():
    """
    Displays the shopping list manager menu with the current date and time.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nShopping List Manager - {current_time}")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Error: Item name cannot be empty.")
        
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"Error: '{item}' not found in the shopping list.")
        
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("Shopping list is empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()from datetime import datetime

def display_menu():
    """
    Displays the shopping list manager menu with the current date and time.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nShopping List Manager - {current_time}")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Error: Item name cannot be empty.")
        
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"Error: '{item}' not found in the shopping list.")
        
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("Shopping list is empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
