class Piece :
    def __init__(self, board, piece_color, piece_position):
        self.board = board
        self.piece_color = piece_color
        self.piece_position = piece_position

    def forced_move(self, to):
        """
        Move piece from self.piece_position to given position even if given position is not in valid moves
        """

        self.board.position_dict[self.piece_position].piece = None
        self.board.position_dict[to].piece = self
        self.piece_position = to

    def move(self, to):
        """
        Move piece from self.piece_position to given position if given position is in valid moves
        """
        
        if to not in self.get_moves():
            raise ValueError("Not a valid move!! ")
        
        self.forced_move(to)
