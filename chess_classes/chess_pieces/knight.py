from ..vars import pos_tuple
from ..piece import Piece

class Knight(Piece):
    """
    Creates a knight object for given board, with given piece color and piece position
    """
    def __init__(self, board, piece_color, piece_position):
        """
        board: board object
        piece_color: color of the piece
        piece_position: position code of the piece
        """ 
        super().__init__(board, piece_color, piece_position)
    
    def get_moves(self):
        """
        Get all possible moves of the piece
        """
        valid_moves_knight = []
        x = ord(self.piece_position[0])
        y = int(self.piece_position[1])
        if self.piece_color == "white": 
            pass