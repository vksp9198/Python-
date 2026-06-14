import json

def load_from_file():
    try:
        with open("student_data.json" , "r") as file:
            students = json.load(file)
        # print("\nData loaded successfully!")
        # print(students)
        return students
    except FileNotFoundError:
        print("No existing data found!, starting fresh")
        return []       

def save_to_file(students):
    # load_from_file(students)
    with open("student_data.json" , "w") as file:
        json.dump(students ,file , indent=4)
    # print("Data saved successfully in student_data.json file")

def view_all_student(students):
    # print(students)
    # print(type(students))
    print("-" * 40 ,"Student Records", "-" * 40)
    for key , data in students.items():
    # print(key , data , type(data))
        print(f"Student roll : {key}  | Name : {data["name"]}  | Age : {data["age"]}  | Grade : {data["grade"]}")
    print("-" * 102)
    
def search_student(students):
    roll = input("Enter Student Roll : ")
    if roll in students:
        # print(roll)
        print("-" * 40 ,"Student Information", "-" * 40)
        print(f"Student roll : {roll}  | Name : {students[roll]["name"]}  | Age : {students[roll]["age"]}  | Grade : {students[roll]["grade"]}")
        print("-" * 102)
    else:
        print("Student Not found!!")

def delete_student(students):
    roll = input("Enter Student Roll : ")
    if roll in students:
        std_name = students[roll]["name"]
        del students[roll]
        print(f"Student {std_name} Deleted successfully!")
    else:
       print("Student NOT found!!")
    save_to_file(students)
    
def update_student(students):
    roll = input("Enter Student Roll : ")
    # for key ,data in students.items():
    #     print(f"{key} : {data}")
    #     print(f"{type(key)} : {type(data)}")

    if roll in students:
        # print(roll)
        print("---Now you can update Student data---")
        students[roll]["name"] = input("New name : ")
        students[roll]["age"] = input("New age : ")
        students[roll]["grade"] = input("New grade : ")
    # print(students)
        print(f"Student data [{students[roll]["name"]}] Updated successfully!")
    else:
        print("Student Not found!!")
   
    save_to_file(students)

def add_student(students):
    while True:
        try:
            std_id = int(input("Enter your roll : "))
            break
        except ValueError:
            print("ID must be a number!")

    while True:
        try:
            std_name = input("Enter your name : ")
            break
        except ValueError:
            print("Name must contain only letters!")

    while True:
        try:
            std_age = int(input("Enter your age : "))
            break
        except ValueError:
            print("Age must be a number!")
            
    std_grade = input("Enter your Grade : ")
    
    students[std_id] = {
            "name" : std_name,
            "age" : std_age,
            "grade" : std_grade
        }
    
    print(f"Student {std_name} Added successfully!")
    # print(students)
    save_to_file(students)
    

def main():
    students = load_from_file() 
    # print(students)
    while True:
        print("=====Student Management System=====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. View All Students")
        print("6. Exit")

        choice = input("Enter your choice : ")

        match choice:
            case '1' : add_student(students)
            case '2' : update_student(students)
            case '3' : delete_student(students)
            case '4' : search_student(students)
            case '5' : view_all_student(students)
            case '6' :break
            case _:
                print("Invalid choice!!, Try again.")

if __name__ == "__main__":
    main()
