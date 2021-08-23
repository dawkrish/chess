from .classes import User
from ..database.create import create_game, create_user
from ..database.get import get

def authenticate():
    while True:
        option = input("""Enter 1 to login
      2 to signup
      3 to exit

> """)

        if option in ['1', '2', '3']:
            break
    
    if option == '3':
        exit()
    
    if option == '2':
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        while True:
            try:
                create_user(username, password)
            except ValueError as e:
                print("\n", e, "\n", sep="")
                return authenticate()
            else:
                break
        
        return User(username)
    
    if option == '1':
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        res = get("users", f"username = '{username}' and password = '{password}'")

        if len(res) != 1:
            print("\nInvalid Credentials\n")
            return authenticate()
        
        return User(username)
