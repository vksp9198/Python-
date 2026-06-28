import sqlite3
conn = sqlite3.connect('student_data.db')
cur = conn.cursor()

cur.execute(""" 
    CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,
            name TEXT NOT NULL, 
            dept TEXT NOT NULL)
""")   # starting of all database querry.

def add_student(id,name, dept):
    cur.execute("INSERT INTO student (id, name, dept) VALUES (?,?,?)",(id , name , dept))
    conn.commit()
    print("-----student Added successfully-----")

def update_student(id,name ,dept):
    cur.execute("UPDATE student SET name = ? , dept = ? WHERE id = ? ", (name, dept,id))
    conn.commit()
    print("-----student Updated successfully-----")

def delete_student(id):
    cur.execute("DELETE FROM student WHERE id = ? ", (id,))
    conn.commit()
    print("-----student Deleted successfully-----")

def search_student(id):
    cur.execute("SELECT * FROM student WHERE id = ? ", (id,))
    print(cur.fetchone())
    conn.commit()
          
def view_all_student():
    cur.execute("SELECT * FROM student")
    for row in cur.fetchall():
        print(row)

def main():
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
            case '1' : 
                print("-----Add student data-----")
                id = input("Enter your roll number : ")
                name = input("Enter your Name : ")
                dept = input("Enter your Department : ")
                add_student(id, name, dept)
            case '2' : 
                print("-----Update student data-----")
                id = input("Enter your roll number : ")
                name = input("Enter your Name : ")
                dept = input("Enter your Department : ")
                update_student(id, name ,dept)
            case '3' : 
                print("-----Delete student data-----")
                id = input("Enter your roll number : ")
                delete_student(id)
            case '4' : 
                print("-----Search student data-----")
                id = input("Enter your roll number : ")
                search_student(id)
            case '5' : 
                print("-----All student data-----")
                view_all_student()
            case '6' :
                print("Goodbye!!!")
                break
            case _:
                print("Invalid choice!!, Try again.")

if __name__ == "__main__":
    main()