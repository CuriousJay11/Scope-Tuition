import json

student = {
    "name": "Albus Severus Potter",
    "marks": 100
}

json_data = json.dumps(student)
print(json_data)

print(type(json_data))

students = '{"name": "James Sirius Potter", "marks": 99}'

a_data = json.loads(students)
print(a_data)


with open("student.json","w") as file:json.dump(student,file)

with open("student.json","r") as file:
    data = json.load (file)
print(data)