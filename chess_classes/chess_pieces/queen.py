from ..vars import pos_tuple
from ..piece import Piece
from .king import King

class Queen(Piece):
    """
    Creates a queen object for given board, with given piece color and piece position
    """
    def __init__(self, board, piece_color, piece_position):
        """
        board: board object
        piece_color: color of the piece
        piece_position: position code of the piece
        """ 
        super().__init__(board, piece_color, piece_position)

    def get_moves(self):
        valid_moves_queen = []
        x = ord(self.piece_position[0])
        y = int(self.piece_position[1])

        if self.piece_color == "white":
            # up left loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x - 1
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
                break
            # up right loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x + 1
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                    piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
                break
            #down right loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x + 1
                new_y = new_y - 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
                break
            #down left loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x - 1
                new_y = new_y -1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
                break
            
            #up loop  
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
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
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
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
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
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos) 
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
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "black" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos) 
                break


        if self.piece_color == "black":
            # up left loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x - 1
                new_y = new_y - 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
                break
            # up right loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x + 1
                new_y = new_y - 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
                break

            #down right loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x + 1
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
                break

            #down left loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x - 1
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is None:
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
                break
            
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
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
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
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos)
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
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos) 
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
                    valid_moves_queen.append(new_pos)
                    continue
                if piece_at_new_position.piece_color == "white" and type(piece_at_new_position) != King:
                    valid_moves_queen.append(new_pos) 
                break

        return valid_moves_queen

    def get_moves_for_king(self):
        """
        Get the moves where opposite color king cannot move
        """

        invalid_moves_for_king = []
        x = ord(self.piece_position[0])
        y = int(self.piece_position[1])

        if self.piece_color == "white":
            # up  loop
            new_x = x
            new_y = y
            # Includes every move and breaks the loop when a piece is encountered
            while True:
                new_x = new_x  
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
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
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break

            # down loop
            new_x = x
            new_y = y
            while True:                 
                new_x = new_x  
                new_y = new_y - 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
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
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break
            # up left loop
            new_x = x
            new_y = y
            # Includes every move and breaks the loop when a piece is encountered
            while True:
                new_x = new_x - 1
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break

            # up right loop  
            new_x = x
            new_y = y
            while True:                
                new_x = new_x + 1
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break
            # down right loop
            new_x = x
            new_y = y
            while True:                 
                new_x = new_x + 1
                new_y = new_y - 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break
            # down left loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x - 1
                new_y = new_y -1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break
        
        if self.piece_color == "black":
            # up  loop
            new_x = x
            new_y = y
            # Includes every move and breaks the loop when a piece is encountered
            while True:
                new_x = new_x 
                new_y = new_y - 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
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
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break
            # down loop
            new_x = x
            new_y = y
            while True:                 
                new_x = new_x 
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
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
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break
            
            # up left loop
            new_x = x
            new_y = y
            # Includes every move and breaks the loop when a piece is encountered
            while True:
                new_x = new_x - 1
                new_y = new_y - 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break

            # up right loop  
            new_x = x
            new_y = y
            while True:                
                new_x = new_x + 1
                new_y = new_y - 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break
            # down right loop
            new_x = x
            new_y = y
            while True:                 
                new_x = new_x + 1
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break
            # down left loop
            new_x = x
            new_y = y
            while True:
                new_x = new_x - 1
                new_y = new_y + 1
                new_pos = f"{chr(new_x)}{new_y}"
                if new_pos not in pos_tuple:
                    break
                invalid_moves_for_king.append(new_pos)
                piece_at_new_position = self.board.position_dict[new_pos].piece
                if piece_at_new_position is not None:
                    break

        return invalid_moves_for_king

    def __str__(self):
        return f"{self.piece_color[0]}q"

        