Bucketlist = []  # Show, Add(Append), Remove(.remove), Search(if in)


def show_list():
    if len(Bucketlist) == 0:
        print("List is empty")
    else:
        print("\nBucketList:")
        i = 1
        for item in Bucketlist:
           print(i, item)
           i += 1

def add_item():
    item = input("Enter item to add: ")
    if item in Bucketlist:
        print("Item already exists")
    else:
        Bucketlist.append(item)
        print("Added")

def remove_item():
    item = input("Enter item to remove: ")
    if item in Bucketlist:
        Bucketlist.remove(item)
        print("Removed")
    else:
        print("Item not found")


def search_item():
    item = input("Enter item to search: ")
    if item in Bucketlist:
        print("Found")
    else:
        print("Not found")

while True:
    print("\nBucket List")
    print("1. Show List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Search Item")

    choice = input("Choose: ")

    if choice == "1":
        show_list()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        search_item()
    else:
        print("Invalid Choice")

    
