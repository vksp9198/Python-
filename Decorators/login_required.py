def login_required(func):
    def wrapper(user):
        if not user.get("logged_in"):
            print("Access Denied!!")
            return
        return func(user)
    return wrapper

@login_required
def profile(user):
    print(f"Welcome , {user["name"]}")
profile({"name" : "Vikas" , "logged_in" : False})