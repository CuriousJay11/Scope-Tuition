grocery = ["Milk", "Bread", "Eggs"]


def show_list():
    if len(grocery) == 0:
        print("List is empty")
    else:
        print("\nGrocery List:")
        i = 1
        for item in grocery:
           print(i, item)
           i += 1


def add_item():
    item = input("Enter item to add: ")
    if item in grocery:
        print("Item already exists")
    else:
        grocery.append(item)
        print("Added")


def insert_item():
    item = input("Enter item to insert: ")
    pos = int(input("Enter position (0-based index): "))
    grocery.insert(pos, item)
    print("Inserted")


def remove_item():
    item = input("Enter item to remove: ")
    if item in grocery:
        grocery.remove(item)
        print("Removed")
    else:
        print("Item not found")


def remove_last():
    if len(grocery) == 0:
        print("List is empty")
    else:
        removed = grocery.pop()
        print("Removed:", removed)


def search_item():
    item = input("Enter item to search: ")
    if item in grocery:
        print("Found")
    else:
        print("Not found")


def clear_list():
    grocery.clear()
    print("List cleared")


while True:
    print("\n--- Grocery Menu ---")
    print("1. Show List")
    print("2. Add Item")
    print("3. Insert Item")
    print("4. Remove Item")
    print("5. Remove Last Item")
    print("6. Search Item")
    print("7. Clear List")
    print("8. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_list()
    elif choice == "2":
        add_item()
    elif choice == "3":
        insert_item()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        remove_last()
    elif choice == "6":
        search_item()
    elif choice == "7":
        clear_list()
    elif choice == "8":
        print("Goodbye")
        break
    else:
        print("Invalid choice")