
class Piece :
    def __init__(self, board, piece_color, piece_position):
        self.board = board # Board on which the piece is put
        self.piece_color = piece_color # Color of the piece
        self.piece_position = piece_position # Code of the position at which the piece is put

    def forced_move(self, to):
        """
        Move piece from self.piece_position to given position even if given position is not in valid moves
        """

        # Remove the piece from it's original position
        self.board.position_dict[self.piece_position].piece = None
        # Put the piece on thr given 'to' position
        self.board.position_dict[to].piece = self
        # Update the name of the position at which the piece is
        self.piece_position = to

    def move(self, to):
        """
        Move piece from self.piece_position to given position if given position is in valid moves
        """

        # Check if the given 'to' position is a valid move        
        if to not in self.get_moves():
            raise ValueError("Not a valid move!! ")
        
        # Move the piece
    
        self.forced_move(to)


