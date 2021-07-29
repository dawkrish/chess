from ..vars import pos_tuple
from ..piece import Piece
from .king import King

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
                if ldp.piece is not None and ldp.piece.piece_color == "black" and type(ldp.piece) != King:
                    valid_moves_pawn.append(left_diagonal_position)
            
            if right_diagonal_position in pos_tuple:
                rdp = self.board.position_dict[right_diagonal_position]
                if rdp.piece is not None and rdp.piece.piece_color == "black" and type(rdp.piece) != King:
                    valid_moves_pawn.append(right_diagonal_position)
            
            if y == 2:
                fp = self.board.position_dict[front_position]
                if fp.piece is None:
                    fmp = self.board.position_dict[f"{chr(x)}{y + 2}"]
                    if fmp.piece is None and type(fp.piece != King):
                        valid_moves_pawn.append(f"{chr(x)}{y + 2}")
            
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
                if ldp.piece is not None and ldp.piece.piece_color == "white" and type(ldp.piece) != King:
                    valid_moves_pawn.append(left_diagonal_position)
            
            if right_diagonal_position in pos_tuple:
                rdp = self.board.position_dict[right_diagonal_position]
                if rdp.piece is not None and rdp.piece.piece_color == "white" and type(rdp.piece) != King:
                    valid_moves_pawn.append(right_diagonal_position)

            if y == 7:
                fp = self.board.position_dict[front_position]
                if fp.piece is None:
                    fmp = self.board.position_dict[f"{chr(x)}{y - 2}"]
                    if fmp.piece is None:
                        valid_moves_pawn.append(f"{chr(x)}{y - 2}")
        
        for pos in pos_tuple:
            position = self.board.position_dict[pos]
            if position.piece is not None and type(position.piece) == King and position.piece.piece_color == self.piece_color:
                my_king = position.piece
                break

        if my_king.is_in_check():
            new_valid_moves_pawn = []
            initial_position = self.piece_position
            for final_position in valid_moves_pawn:
                piece_already_at_final_position = self.board.position_dict[final_position].piece
                self.forced_move(final_position)
                if not my_king.is_in_check():
                    new_valid_moves_pawn.append(final_position)
                self.forced_move(initial_position)
                self.board.position_dict[final_position].piece = piece_already_at_final_position
            return new_valid_moves_pawn

        return valid_moves_pawn
    
    def get_invalid_moves_for_opposite_king(self):
        """
        Get the moves where opposite color king cannot move
        """

        invalid_moves_for_king = []
        x = ord(self.piece_position[0])
        y = int(self.piece_position[1])

        if self.piece_color == "white":
            left_diagonal_position = f"{chr(x-1)}{y+1}"
            right_diagonal_position = f"{chr(x+1)}{y+1}"

        if self.piece_color == "black":
            left_diagonal_position = f"{chr(x-1)}{y-1}"
            right_diagonal_position = f"{chr(x+1)}{y-1}"

        if left_diagonal_position in pos_tuple:
            invalid_moves_for_king.append(left_diagonal_position)
        if right_diagonal_position in pos_tuple:
            invalid_moves_for_king.append(right_diagonal_position)

        return invalid_moves_for_king

    def __str__(self):
        return f"{self.piece_color[0]}p"
