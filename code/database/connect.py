from .config import *
import mysql.connector


def connect():
    '''
    Connects to local host of this machine
    '''

    connection = mysql.connector.connect(
        database = DATABASE,
        user = USER,
        passwd = PASSWORD,
        host = HOST
    )

    return connection
