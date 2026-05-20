def shopping(*items,**details):
    print("Items:")
    for i in items:
        print(i)
    print(("\nDetails:"))
    for key,value in details.items():
        print(key,":",value)
shopping("Shoes","Watches","Bag",name="Vijay",city="Houston")
