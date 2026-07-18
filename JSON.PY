import json

student = {
    "name": "Alex",
    "marks": 85
}


json_data = json.dumps(student)
print(json_data)

print(type(json_data))

students = '{"name": "Steve", "marks": 85}'

a_data = json.loads(students)
print(a_data)


 