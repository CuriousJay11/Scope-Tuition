# Two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("A - B:", A - B)

# Symmetric Difference
print("Symmetric Difference:", A ^ B)

# Add an element
A.add(7)
print("After adding 7 to A:", A)

# Remove an element
A.remove(2)
print("After removing 2 from A:", A)

# Check membership
print("Is 5 in B?", 5 in B)

# Subset and Superset
print("A is subset of B:", A.issubset(B))
print("A is superset of B:", A.issuperset(B))