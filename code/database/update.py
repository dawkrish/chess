from .connect import connect
from .get import get


def update_moves(game_ID,new_moves):
    '''
    Updates the moves of the game of given ID
    Shows error if game ID is invalid
    '''
    res = get("games",f"ID = {game_ID}")
    if len(res) != 1:
        raise ValueError("invalid game ID")

    command = f"UPDATE GAMES SET moves = '{new_moves}' WHERE ID = {game_ID}" 
    
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()
