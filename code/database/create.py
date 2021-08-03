from .connect import connect
from .get import get

def create_user(new_username, new_password): 
    '''
    Creates a user with given user and password 
    It raises error if the username is already used
    '''

    new_username = new_username.lower()
    res = get("users", f"username = '{new_username}'")

    if len(res) > 0:
        raise ValueError("username already used")
    
    command = f"INSERT INTO USERS (username,password) VALUES ('{new_username}', '{new_password}')"
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(command)
    connection.commit()

def create_game(user1, user2):
    '''
    Creates a games with given users {user1 and user2} 
    It raises error if invalid usernames are given
    '''
    
    res = get("users", f"username = '{user1}' or username = '{user2}'", 2)
    if len(res) < 2:
        raise ValueError("Invalid usernames!")   
    
    command = f"INSERT INTO GAMES (user1, user2, moves) VALUES ('{user1}', '{user2}', '')"

    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute(command)
    connection.commit()




