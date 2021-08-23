from .config import *
import mysql.connector


CONNECTION = None

def connect():
    '''
    Connects to local host of this machine
    '''
    global CONNECTION


    if CONNECTION is not None: return CONNECTION

    CONNECTION = mysql.connector.connect(
        database = DATABASE,
        user = USER,
        passwd = PASSWORD,
        host = HOST
    )

    return CONNECTION
