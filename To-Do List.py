passengers = ["John", "Emma", "Michael"]


def show_passengers():
    if len(passengers) == 0:
        print("Passenger list is empty")
    else:
        print("\nPassenger List:")
        i = 1
        for passenger in passengers:
            print(i, passenger)
            i += 1


def add_passenger():
    name = input("Enter passenger name to add: ")
    if name in passengers:
        print("Passenger already exists")
    else:
        passengers.append(name)
        print("Passenger added")


def insert_passenger():
    name = input("Enter passenger name to insert: ")
    pos = int(input("Enter position (0-based index): "))
    passengers.insert(pos, name)
    print("Passenger inserted")


def remove_passenger():
    name = input("Enter passenger name to remove: ")
    if name in passengers:
        passengers.remove(name)
        print("Passenger removed")
    else:
        print("Passenger not found")


def remove_last_passenger():
    if len(passengers) == 0:
        print("Passenger list is empty")
    else:
        removed = passengers.pop()
        print("Removed:", removed)


def search_passenger():
    name = input("Enter passenger name to search: ")
    if name in passengers:
        print("Passenger found")
    else:
        print("Passenger not found")


def clear_passengers():
    passengers.clear()
    print("Passenger list cleared")


while True:
    print("\n--- Flight Passenger Menu ---")
    print("1. Show Passengers")
    print("2. Add Passenger")
    print("3. Insert Passenger")
    print("4. Remove Passenger")
    print("5. Remove Last Passenger")
    print("6. Search Passenger")
    print("7. Clear Passenger List")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_passengers()
    elif choice == "2":
        add_passenger()
    elif choice == "3":
        insert_passenger()
    elif choice == "4":
        remove_passenger()
    elif choice == "5":
        remove_last_passenger()
    elif choice == "6":
        search_passenger()
    elif choice == "7":
        clear_passengers()
    elif choice == "8":
        print("Thank you for using the Flight Passenger Management System!")
        break
    else:
        print("Invalid choice. Please try again.")