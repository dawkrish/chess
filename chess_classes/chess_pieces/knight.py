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
            up_left = f"{chr(x-1)}{y+2}"
            up_right = f"{chr(x+1)}{y+2}"
            left_up = f"{chr(x-2)}{y+1}"
            right_up = f"{chr(x+2)}{y+1}"
            
            down_left = f"{chr(x-1)}{y-2}"
            down_right = f"{chr(x+1)}{y-2}"
            left_down = f"{chr(x-2)}{y-1}"
            right_down = f"{chr(x+2)}{y-1}"

            if up_left in pos_tuple:
                ul = self.board.position_dict[up_left]
                if ul.piece is None or ul.piece.piece_color == "black":
                    valid_moves_knight.append(up_left)

            if up_right in pos_tuple:
                ur = self.board.position_dict[up_left]
                if ur.piece is None or ur.piece.piece_color == "black":
                    valid_moves_knight.append(up_right)

            if left_up in pos_tuple:
                lu = self.board.position_dict[left_up]
                if lu.piece is None or lu.piece.piece_color == "black":
                    valid_moves_knight.append(left_up)
                    
            if right_up in pos_tuple:
                ru = self.board.position_dict[right_up]
                if ru.piece is None or ru.piece.piece_color == "black":
                    valid_moves_knight.append(right_up)            
            
            if down_left in pos_tuple:
                dl = self.board.position_dict[down_left]
                if dl.piece is None or dl.piece.piece_color == "black":
                    valid_moves_knight.append(down_left)

            if down_right in pos_tuple:
                dr = self.board.position_dict[down_right]
                if dr.piece is None or dr.piece.piece_color == "black":
                    valid_moves_knight.append(down_right)

            if left_down in pos_tuple:
                ld = self.board.position_dict[left_down]
                if ld.piece is None or ld.piece.piece_color == "black":
                    valid_moves_knight.append(left_down)
                    
            if right_down in pos_tuple:
                rd = self.board.position_dict[right_down]
                if rd.piece is None or rd.piece.piece_color == "black":
                    valid_moves_knight.append(right_down)

        if self.piece_color == "black":
            up_left = f"{chr(x-1)}{y-2}"
            up_right = f"{chr(x+1)}{y-2}"
            left_up = f"{chr(x-2)}{y-1}"
            right_up = f"{chr(x+2)}{y-1}"

            down_left = f"{chr(x-1)}{y+2}"
            down_right = f"{chr(x+1)}{y+2}"
            left_down = f"{chr(x-2)}{y+1}"
            right_down = f"{chr(x+2)}{y+1}"
            
            if up_left in pos_tuple:
                ul = self.board.position_dict[up_left]
                if ul.piece is None or ul.piece.piece_color == "white":
                    valid_moves_knight.append(up_left)
            
            if up_right in pos_tuple:
                ur = self.board.position_dict[up_right]
                if ur.piece is None or ur.piece.piece_color == "white":
                    valid_moves_knight.append(up_right)

            if left_up in pos_tuple:
                lu = self.board.position_dict[left_up]
                if lu.piece is None or lu.piece.piece_color == "white":
                    valid_moves_knight.append(left_up)

            if right_up in pos_tuple:
                ru = self.board.position_dict[right_up]
                if ru.piece is None or ru.piece.piece_color == "white":
                    valid_moves_knight.append(right_up)

            if down_left in pos_tuple:
                dl = self.board.position_dict[down_left]
                if dl.piece is None or dl.piece.piece_color == "white":
                    valid_moves_knight.append(down_left)

            if down_right in pos_tuple:
                dr = self.board.position_dict[down_right]
                if dr.piece is None or dr.piece.piece_color == "white":
                    valid_moves_knight.append(down_right)
    
            if left_down in pos_tuple:
                ld = self.board.position_dict[left_down]
                if ld.piece is None or ld.piece.piece_color == "white":
                    valid_moves_knight.append(left_down)
                    
            if right_down in pos_tuple:
                rd = self.board.position_dict[right_down]
                if rd.piece is None or rd.piece.piece_color == "white":
                    valid_moves_knight.append(right_down)
        
        return valid_moves_knight
    
    def get_moves_for_king(self):
        return []
    
    def __str__(self):
        return f"{self.piece_color[0]}h"