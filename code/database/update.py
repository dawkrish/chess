from .connect import connect
from .get import get


def join_game(game_id, user):
    '''
    Join a game using given game_id and user (also game_pass if mode = 'private')
    '''

    res = get("games", f"ID = {game_id} and status = 'open'")
    if len(res) != 1:
        raise ValueError("Invald Game")

    command = f"UPDATE games SET status = 'running', user2 = '{user.username}' WHERE ID = {game_id}"

    connection = connect()
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()

def update_game(game_ID, updates):
    '''
    Updates the moves of the game of given ID
    Shows error if game ID is invalid
    '''

    res = get("games",f"ID = {game_ID}")
    if len(res) != 1:
        raise ValueError("invalid game ID")

    command = f"UPDATE games SET {updates} WHERE ID = {game_ID}" 
    
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()
