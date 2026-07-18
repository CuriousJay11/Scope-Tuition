import numpy as np

customer = np.array(["Alex","Rio","Manny","Leo"])
purchase = np.array([1200,800,2500,1500])

print("Customers:", customer)
print("Purchase:", purchase)
print("Total Sale:", np.sum(purchase))
print("Highest Purchase:", customer[np.argmax(purchase)])
print("Lowest Purchase:", customer[np.argmin(purchase)])
print("Above 1200:", customer[purchase > 1200])
print("Sorted:", np.sort(purchase))

print("\nPurchase Type")
for i in range(len(customer)):
    print(customer[i], "Big" if purchase[i] > 1200 else "Small")

print("\nStatus")
for i in range(len(customer)):
    if purchase[i] >= 2000:
        status = "Gold"
    elif purchase[i] >= 1000:
        status = "Silver"
    else:
        status = "Bronze"
        
    print(customer[i], status)
