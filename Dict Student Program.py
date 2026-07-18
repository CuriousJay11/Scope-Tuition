


student = {
    "name": "John",
    "age": 20,
    "course": "Python",
    "year": 2024,
    "year": 2025  
}


print("Name:", student["name"])
print("Course:", student.get("course"))

print("\nDictionary:", student)
print("Number of items:", len(student))


print("\nKeys:", student.keys())


student["grade"] = "A"
print("After adding grade:", student)


print("\nValues:", student.values())


print("Items:", student.items())


if "course" in student:
    print("\nCourse key exists.")
else:
    print("\nCourse key does not exist.")


student["age"] = 21
print("\nUpdated age:", student)


student.update({"year": 2026})
print("Updated year:", student)