# json.py

import json

# Example 1: JSON string to Python (loads)
json_string = '{"name": "Dias", "age": 20}'
data = json.loads(json_string)
print("Name:", data["name"])


# Example 2: Python to JSON string (dumps)
person = {"city": "Almaty", "country": "Kazakhstan"}
json_output = json.dumps(person)
print("JSON string:", json_output)


# Example 3: Writing JSON to file
student = {
    "name": "Ali",
    "age": 21,
    "grades": [90, 85, 88]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)


# Example 4: Reading JSON from file
with open("student.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded student:", loaded_data)


# Example 5: Working with list of JSON objects
students = [
    {"name": "Sara", "age": 19},
    {"name": "Omar", "age": 22}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    data_list = json.load(file)

for student in data_list:
    print(student["name"])