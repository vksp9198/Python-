students = {}

marks = []
while True: 
    print("\n---------Student Grade Management System--------\n")
    std_roll = input("Enter your roll = ")
    std_name = input("Enter your name = ")

    for i in range(3):
        mark = int(input(f"Enter marks of subject {i + 1}: "))
        marks.append(mark)
    # print(marks)

    # total marks
    total = sum(marks)
    # print(total)

    #Average marks
    avg_marks = round(total/(len(marks)),2)
    # print(avg_marks)

    # grade calculation
    grade = ""
    if total >= 280:
        grade = "A - Grade"
    elif total >= 230:
        grade = "B - Grade"
    elif total >= 170:
        grade = "C - Grade"
    else:
        grade = "Fail!!"

    # store data in dictionary
    students[std_roll] = {
        "name" : std_name,
        "marks" : marks,
        "total_marks" : total,
        "average_marks" : avg_marks,
        "grade" : grade
    }
    #print(students)

    # dictionary data handling 
    for key , data in students.items():
        print("\n-------Student Record -------")
        print(f"Id : {key}")
        print(f"Name : {data["name"]}")
        print(f"Marks : {data["marks"]}")
        print(f"Total Marks : {data["total_marks"]}")
        print(f"Average Marks : {data["average_marks"]}")
        print(f"Grade : {data["grade"]}")
        print("-----------------------------")
    break