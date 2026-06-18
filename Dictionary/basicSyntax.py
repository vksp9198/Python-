# Dictionary: "A Dictionary in pyhton stores data key : value pairs"
student = {
    "name" : "Vikas",
    "age" : 19,
    "marks" : 89
}

# how to accesss keys 
for key in student:
    print(f"key is : {key}")
    print()


# how to accesss values 
for value in student.values():
    print(f"value is : {value}")
    print()

# key value both

for key , value in student.items():
    print(f"Key: {key} , Value : {value}")
    print()

# if you know keys then 
print(student["name"])
print(student["age"])
print(student["marks"])

#Accessing Data using get() [better and saffer way]
print("*" * 44)
# print(student.get("mark", "Student Not found" ))

#Adding data in student 
student["grade"] = "A+"
# print(student.get("grade" , "Student not found"))

#update data in student 
student["name"] = "Prajapati"
# print(student.get("name" , "Student not found"))

# Removing data 
student.pop("marks")
# using del keyword 
del student["age"]

# using clear() method we can delete/ clear all student data 
student.clear()
for k, v in student.items():
    print(f"key : {k}, value : {v}")

# it's all about dictionary how add , remove , update data in dictonary also clear entire dictionary as well. 

