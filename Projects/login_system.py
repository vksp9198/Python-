import json
def load_data():
    try:
        with open("user_data.json", "r") as file:
            user_data = json.load(file)
            print(user_data)
            return user_data
            
    except FileNotFoundError:
        print("File not found! , Create new one.")
        return {}
    
def save_user_info(users):
    with open("user_data.json" , "w") as file:
        json.dump(users , file, indent=4)

def validate_password(pwd):
    if len(pwd) < 4:
        return False
    if not any(char.isdigit() for char in pwd):
        return False
    return True
    


def user_register():
    users = load_data()
    username = input("Enter user name: ")
    if username in users:
        print("User already exists!!")
        return
    password = input("Enter password: ")
    if not validate_password(password):
        print("Weak password, Try again!")
        return
    users[username] = password
    save_user_info(users)
    print(users)
    print("User Registered successfully!!")

def user_login():
    users = load_data()
    user_name = input("Enter Name: ").strip()
    user_pass = input("Enter Password: ").strip()

    if user_name in users and users[user_name] == user_pass:
        print("Login successfull!! , Welcome", user_name)
    else:
        print("Invalid username and password!!")

def change_password():
    users = load_data()
    user_name = input("Enter Name: ").strip()
    if user_name in users:
        old_pass = input("Enter Old Password: ").strip()
        if users[user_name] == old_pass:
            new_pass = input("Enter New Password: ").strip()
            if validate_password(new_pass):
                users[user_name] = new_pass
                save_user_info(users)
            print("Password changed successfully!!")
        else:
            print("Incorrect old password!!!, Try again.")
    else:
        print("User NOT found!!")


def forgot_password():
    users = load_data()
    user_name = input("Enter Name: ").strip()
    if user_name in users:
        DOB = input("Enter your Date of Birth: ")
        if DOB == "2006":
            new_pass = input("Enter New Password: ").strip()
            if validate_password(new_pass):
                users[user_name] = new_pass
                save_user_info(users)
                print("Password reset successfully!!")
            else:
                print("Weak password!")
        else:
            print("Incorrect Date of Birth!")
    else:
        print("User NOT found!!")




def main():
    users = load_data()
    while True:
        print("===== USER LOGIN SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. Forgot Password")
        print("5. Exit")

        choice = input("Enter your choice : ")
        match choice:
            case '1' : user_register()
            case '2' : user_login()
            case '3' : change_password()
            case '4' : forgot_password()
            case '5' : 
                print("Goodbye!!")
                break


if __name__ == "__main__":
    main()