from ..vars import pos_tuple
from ..piece import Piece

class Rook(Piece):
    """
    Creates a rook object for given board, with given piece color and piece position
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
        valid_moves_rook = []
        x = ord(self.piece_position[0])
        y = int(self.piece_position[1])
        
        if self.piece_color == "white":
            # up loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x 
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_rook.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black":
                    valid_moves_rook.append(new_pos)
                break
            
            #down loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x 
                new_y = new_y - 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_rook.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black":
                    valid_moves_rook.append(new_pos)
                break

            # right loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x + 1
                new_y = new_y
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_rook.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black":
                    valid_moves_rook.append(new_pos) 
                break    
            # left loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x - 1
                new_y = new_y 
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_rook.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black":
                    valid_moves_rook.append(new_pos) 
                break

        elif self.piece_color == "black":
            # up loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x 
                new_y = new_y - 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_rook.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white":
                    valid_moves_rook.append(new_pos)
                break
            
            #down loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x 
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_rook.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white":
                    valid_moves_rook.append(new_pos)
                break

            # right loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x + 1
                new_y = new_y 
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_rook.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white":
                    valid_moves_rook.append(new_pos) 
                break    
            # left loop
            new_x = x 
            new_y = y
            while True:
                new_x = new_x - 1
                new_y = new_y 
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_rook.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white":
                    valid_moves_rook.append(new_pos) 
                break
            

        return valid_moves_rook
        
    def __str__(self):
        return f"{self.piece_color[0]}r"