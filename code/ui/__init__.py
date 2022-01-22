from ..database.setup import setup
from .auth import authenticate
from .game import start_game

def start():
    setup()
    myuser = authenticate()
    start_game(myuser)
