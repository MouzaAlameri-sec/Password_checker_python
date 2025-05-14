__Author__ = "Mouza Alameri"
__Date__ ="14/05/2025"


def access_control(func):
    def wrapper(user):
        if user == "Admin":
            print("Okay ml, you can view this.")
            func(user)
        else:
            print(" No access granted. Only Admin can view this.")
    return wrapper

@access_control
def viewsec(user):
    print(" The secret is 1234")

user_input = input("Enter your role (Admin/Guest): ")
viewsec(user_input)
