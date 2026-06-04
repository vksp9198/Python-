# file = open("user_data.txt","r")
# content = file.read()
# print(content)
# file.close() 


# better way to read file
# with open("user_data.txt" , "a") as file:
#     file.write("\nthe day you will achive , every day will be become successfull")
    
student = {
    "id" : 117,
    "name" : "Vikas" ,
    "college" : "SCCT"
}

with open("user_data.txt" , "w") as file:
    for key , value in student.items():
        file.write(f"{key} : {value}\n")

with open("user_data.txt" , "r") as file:
        student = {}
        for line in file:
             key , value = line.strip().split(":")
             student[key] = value
        print(student)