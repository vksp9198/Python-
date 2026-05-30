students = {
    "101" : {
        "name" : "Vikas prajapati",
        "course" : {
            "department" : "IT",
            "Python3" : {
                "marks" : "88",
                "trainer" : "Nibha kumari"
            },
            "Java" : {
                "marks" : "88",
                "trainer" : "Quadir Sir"
            },
        },
    },
    "102" : {
        "name" : "Sagar Gond",
        "course" : {
            "department" : "IT",
            "Python3" : {
                "marks" : "94",
                "trainer" : "Nibha kumari"
            },
        },
    }
}

# Accessing vikas python's marks 
for key , value in students.items():
    print(f"{key} : {value["course"]["Python3"]["marks"]}")

# Access priya's trainer name 
print(students["102"]["course"]["Python3"]["trainer"])

# Access java trainer name 
print(students["101"]["course"]["Java"]["trainer"])

#All course of student 101
course_data = students["101"]["course"]

for key , value in course_data.items():
    print(f"{key} : {value}")
    # print(f"{key} : {value["marks"]["trainer"]}")