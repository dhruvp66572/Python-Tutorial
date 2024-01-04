# 1. Create an empty dictionary called Student
Student = {}
print("Student Dictionary: ", Student)

# 2. Add name, color, breed, legs, age to the Student dictionary
Student["name"] = "Dhruv"
Student["age"] = 3
print("\nUpdated Student Dictionary: ", Student)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys for the dictionary
student = {
    "first_name": "Dhruv",
    "last_name": "Prajapati",
    "gender": "Male",
    "age": 19,
    "marital_status": "Single",
    "skills": ["React Js", "Node Js"],
    "country": "India",
    "city": "Anjar",
    "address": "21 chakrava"
}
print("\nStudent Dictionary: ", student)

# 4. Get the length of the student dictionary
length_of_student = len(student)
print("\nLength of Student Dictionary: ", length_of_student)

# 5. Get the value of skills and check the data type, it should be a list
skills_value = student["skills"]
print("\nSkills Value: ", skills_value)
print("Data Type of Skills: ", type(skills_value))

# 6. Modify the skills values by adding one or two skills
student["skills"].extend(["HTML", "CSS"])
print("\nUpdated Skills: ", student["skills"])

# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
print("\nKeys as List: ", keys_list)

# 8. Get the dictionary values as a list
values_list = list(student.values())
print("\nValues as List: ", values_list)

# 9. Change the dictionary to a list of tuples using items() method
items_list = list(student.items())
print("\nItems as List of Tuples: ", items_list)

# 10. Delete one of the items in the dictionary
deleted_item = student.pop("marital_status")
print("\nDeleted Item: ", deleted_item)
print("Updated Student Dictionary: ", student)

# 11. Delete one of the dictionaries
del student
print("\nStudent Dictionary Deleted.")
