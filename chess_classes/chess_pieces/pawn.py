from ..vars import pos_tuple
from ..piece import Piece

class Pawn(Piece):
    """
    Creates a pawn object for given board, with given piece color and piece position
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

        valid_moves_pawn = []
        x = ord(self.piece_position[0])
        y = int(self.piece_position[1])

        if self.piece_color == "white": 
            front_position = f"{chr(x)}{y+1}"
            left_diagonal_position = f"{chr(x-1)}{y+1}"
            right_diagonal_position = f"{chr(x+1)}{y+1}"

            if front_position in pos_tuple:
                fp = self.board.position_dict[front_position]
                if fp.piece is None:
                    valid_moves_pawn.append(front_position)
            
            if left_diagonal_position in pos_tuple:
                ldp = self.board.position_dict[left_diagonal_position]
                if ldp.piece is not None and ldp.piece.piece_color == "black":
                    valid_moves_pawn.append(left_diagonal_position)
            
            if right_diagonal_position in pos_tuple:
                rdp = self.board.position_dict[right_diagonal_position]
                if rdp.piece is not None and rdp.piece.piece_color == "black":
                    valid_moves_pawn.append(right_diagonal_position)
            
        elif self.piece_color == "black":
            front_position = f"{chr(x)}{y-1}"
            left_diagonal_position = f"{chr(x-1)}{y-1}"
            right_diagonal_position = f"{chr(x+1)}{y-1}"
            
            if front_position in pos_tuple:
                fp = self.board.position_dict[front_position]
                if fp.piece is None:
                    valid_moves_pawn.append(front_position)

            if left_diagonal_position in pos_tuple:
                ldp = self.board.position_dict[left_diagonal_position]
                if ldp.piece is not None and ldp.piece.piece_color == "white":
                    valid_moves_pawn.append(left_diagonal_position)
            
            if right_diagonal_position in pos_tuple:
                ldp = self.board.position_dict[right_diagonal_position]
                if ldp.piece is not None and ldp.piece.piece_color == "white":
                    valid_moves_pawn.append(right_diagonal_position)
        
        return valid_moves_pawn
    
    def __str__(self):
        return f"{self.piece_color[0]}p"