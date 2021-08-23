from .connect import connect
from .get import get
from random import randint

def create_user(new_username, new_password): 
    '''
    Creates a user with given user and password 
    It raises error if the username is already used
    '''

    new_username = new_username.lower()
    res = get("users", f"username = '{new_username}'")

    if len(res) > 0:
        raise ValueError("username already used")
    
    command = f"INSERT INTO users (username,password) VALUES ('{new_username}', '{new_password}')"
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(command)
    connection.commit()

def create_game(user):
    '''
    Create a game with given user
    '''

    while True:
        game_id = randint(111111, 999999)
        res = get("games", f"id = {game_id}")
        if len(res) == 0:
            break

    command = f"INSERT INTO games(id, status, user1, moves) VALUES({game_id}, 'open', '{user.username}', '');"

    connection = connect()
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()

    return game_id



