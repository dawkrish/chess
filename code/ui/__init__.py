from .auth import authenticate
from .game import start_game

def start():
    myuser = authenticate()
    start_game(myuser)
