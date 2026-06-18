def search_note():
    line_id = int(input("Enter line number to Search : ").lower())

    try:
        with open("notes.txt" , "r") as file:
            notes = file.readlines()
            # print(notes)
        found = False

        for i, note in enumerate(notes,start=1):
            # print(type(line_id))
            # print(type(i))
            if line_id == i:
                print("*" * 40)
                print(f"-----Searching data------")
                print(f"{i}. {note}")
                print("*" * 40)
                found = True
        if not found:
                print("No matching note found!")
        
    except FileNotFoundError:
        print(f" No notes found! , Create one first.")

def delete_note():
    read_note()
    try:
        line_id = int(input("Entere line number to Deleted : "))
        with open("notes.txt" , "r") as file:
            notes = file.readlines()
            if 1 <= line_id <= len(notes): 
                del notes[line_id - 1] 
                with open("notes.txt" , "w") as file:
                    file.writelines(notes)
                print(f"\nLine number {line_id} Deleted successfully!\n" )
            else:
                print("Invalid line Number!!")

    except Exception as e:
        print(f"Error!! , ",e)        

def update_note():
    read_note()
    try:
        line_id = int(input("Enter line number : "))
        new_note = input("Enter new note : ")

        with open("notes.txt" , "r") as file:
            # print(type(file.readlines()))
            notes = file.readlines()
            # print(notes)
            if 1 <= line_id <= len(notes):
                notes[line_id - 1] = new_note.strip() + "\n"
                with open ("notes.txt" , "w") as file:
                    file.writelines(notes)
                print("\nNote Updated successfully!\n")
            else:
                print(f"Invalid line ID!!")
    except Exception as e:
        print(f"Error! ", e)
        
def read_note():
    try:
        with open("notes.txt" , "r") as file:
            notes = file.readlines()
            if not notes:
                print("Notes NOT found!!")
            else:
                print("-" * 20, "All Notes","-" * 20)
                for i, note in enumerate(notes , start=1):
                    print(f"{i}.{note.strip() + "\n"}")
                print("-" * 60)
    except FileNotFoundError:
        print("No notes found! , Create one first.")

def add_note():
    note = input("Enter note : ")
    try:
        with open("notes.txt" , "a") as file:
            file.write(note + "\n")
        print("\n Note Added successfully!\n")
    except Exception as e:
        print("Error : " , e)



def main():
    while True:
        print("==========NOTES MANAGER==========")
        print("1. Add Note")
        print("2. Read Note")
        print("3. Upadate Note")
        print("4. Delete Note")
        print("5. Search Note")
        print("6. Exit")
        choice = input("Enter your choice : ")
        
        match choice:
            case '1' : add_note()
            case '2' : read_note()
            case '3' : update_note()
            case '4' : delete_note()
            case '5' : search_note()
            case '6' : 
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()