import getpass

USER_DB = {
    "admin": "admin@123",
    "employee": "emp@456"
}

def authenticate(username, password):
    return USER_DB.get(username) == password

def login():
    print("Secure Login System")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if authenticate(username, password):
        print(f"\nWelcome, {username}! You have successfully logged in \n")
    else:
        print("\n Invalid username or password.Access denied \n")

if __name__ == "__main__":
    login()