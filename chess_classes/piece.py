class Piece :
    def __init__(self, board, piece_color, piece_position):
        self.board = board
        self.piece_color = piece_color
        self.piece_position = piece_position
    
    def move(self, to):
        """
        Move piece from self.piece_position to given position
        """
        
        if to not in self.get_moves():
            raise ValueError("Not a valid move!! ")

        self.board.position_dict[self.piece_position].piece = None
        self.board.position_dict[to].piece = self
        self.piece_position = to
