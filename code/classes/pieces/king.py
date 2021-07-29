

from ..vars import pos_tuple
from ..piece import Piece

class King(Piece):
    """
    Creates a king object for given board, with given piece color and piece position
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
        
        valid_moves_king = []
        x = ord(self.piece_position[0])
        y = int(self.piece_position[1])
        
        if self.piece_color == "white":
            left = f"{chr(x-1)}{y}" 
            right = f"{chr(x+1)}{y}"
            up = f"{chr(x)}{y+1}"
            down = f"{chr(x)}{y-1}"
            up_left = f"{chr(x-1)}{y+1}"
            up_right = f"{chr(x+1)}{y+1}"
            down_left = f"{chr(x-1)}{y-1}"
            down_right = f"{chr(x+1)}{y-1}"
            
            invalid_moves = []
            for pos in pos_tuple:
                piece_at_pos = self.board.position_dict[pos].piece
                if piece_at_pos is None:
                    continue
                elif piece_at_pos.piece_color == "black":
                    invalid_moves.extend(piece_at_pos.get_invalid_moves_for_opposite_king())

            if left in pos_tuple and left not in invalid_moves:
                l = self.board.position_dict[left]
                if l.piece is None or l.piece.piece_color == "black":
                    valid_moves_king.append(left)
            
            if right in pos_tuple and right not in invalid_moves:
                r = self.board.position_dict[right]
                if r.piece is None or r.piece.piece_color == "black":
                    valid_moves_king.append(right)  

            if up in pos_tuple and up not in invalid_moves:
                u = self.board.position_dict[up]
                if u.piece is None or u.piece.piece_color == "black":
                    valid_moves_king.append(up)

            if down in pos_tuple and down not in invalid_moves: 
                d = self.board.position_dict[down]
                if d.piece is None or d.piece.piece_color == "black":
                    valid_moves_king.append(down)

            if up_left in pos_tuple and up_left not in invalid_moves:
                ul = self.board.position_dict[up_left]
                if ul.piece is None or ul.piece.piece_color == "black":
                    valid_moves_king.append(up_left)
                    
            if up_right in pos_tuple and up_right not in invalid_moves:
                ur = self.board.position_dict[up_right]
                if ur.piece is None or ur.piece.piece_color == "black":
                    valid_moves_king.append(up_right)
                    
            if down_left in pos_tuple and down_left not in invalid_moves:
                dl = self.board.position_dict[down_left]
                if dl.piece is None or dl.piece.piece_color == "black":
                    valid_moves_king.append(down_left)

            if down_right in pos_tuple and down_right not in invalid_moves:
                dr = self.board.position_dict[down_right]
                if dr.piece is None or dr.piece.piece_color == "black":
                    valid_moves_king.append(down_right)                

        if self.piece_color == "black":
            left = f"{chr(x-1)}{y}"
            right = f"{chr(x+1)}{y}"
            up = f"{chr(x)}{y-1}"
            down = f"{chr(x)}{y+1}"
            up_left = f"{chr(x-1)}{y-1}"
            up_right = f"{chr(x+1)}{y-1}"
            down_left = f"{chr(x-1)}{y+1}"
            down_right = f"{chr(x+1)}{y+1}"

            invalid_moves = []
            for pos in pos_tuple:
                piece_at_pos = self.board.position_dict[pos].piece
                if piece_at_pos is None:
                    continue
                if piece_at_pos.piece_color == "white":
                    invalid_moves.extend(piece_at_pos.get_invalid_moves_for_opposite_king())

            if left in pos_tuple and left not in invalid_moves:
                l = self.board.position_dict[left]
                if l.piece is None or l.piece.piece_color == "white":
                    valid_moves_king.append(left)
            
            if right in pos_tuple and right not in invalid_moves:
                r = self.board.position_dict[right]
                if r.piece is None or r.piece.piece_color == "white":
                    valid_moves_king.append(right)
            
            if up in pos_tuple and up not in invalid_moves:
                u = self.board.position_dict[up]
                if u.piece is None or r.piece.piece_color == "white":
                    valid_moves_king.append(up)
            
            if down in pos_tuple and down not in invalid_moves:
                d = self.board.position_dict[down]
                if d.piece is None or d.piece.piece_color == "white":
                    valid_moves_king.append(down)

            if up_left in pos_tuple and up_left not in invalid_moves:
                ul = self.board.position_dict[up_left]
                if ul.piece is None or ul.piece.piece_color == "white":
                    valid_moves_king.append(up_left)
                
            if up_right in pos_tuple and up_right not in invalid_moves:
                ur = self.board.position_dict[up_right]
                if ur.piece is None or ur.piece.piece_color == "white":
                    valid_moves_king.append(up_right)
            
            if down_left in pos_tuple and down_left not in invalid_moves:
                dl = self.board.position_dict[down_left]
                if dl.piece is None or dl.piece.piece_color == "white":
                    valid_moves_king.append(down_left)
            
            if down_right in pos_tuple and down_right not in invalid_moves:
                dr = self.board.position_dict[down_right]
                if dr.piece is None or dr.piece.piece_color == "white":
                    valid_moves_king.append(down_right)

        return valid_moves_king

    def get_invalid_moves_for_opposite_king(self):
        """
        Get the moves where opposite color king cannot move
        """

        invalid_moves_for_king = []
        x = ord(self.piece_position[0])
        y = int(self.piece_position[1])

        if self.piece_color == "white":
            left = f"{chr(x-1)}{y}"
            right = f"{chr(x+1)}{y}"
            up = f"{chr(x)}{y-1}"
            down = f"{chr(x)}{y+1}"
            up_left = f"{chr(x-1)}{y-1}"
            up_right = f"{chr(x+1)}{y-1}"
            down_left = f"{chr(x-1)}{y+1}"
            down_right = f"{chr(x+1)}{y+1}"
        elif self.piece_color == "black":
            left = f"{chr(x-1)}{y}"
            right = f"{chr(x+1)}{y}"
            up = f"{chr(x)}{y-1}"
            down = f"{chr(x)}{y+1}"
            up_left = f"{chr(x-1)}{y-1}"
            up_right = f"{chr(x+1)}{y-1}"
            down_left = f"{chr(x-1)}{y+1}"
            down_right = f"{chr(x+1)}{y+1}"

        if left in pos_tuple:
            invalid_moves_for_king.append(left)
        if right in pos_tuple:
            invalid_moves_for_king.append(right)
        if up in pos_tuple:
            invalid_moves_for_king.append(up)
        if down in pos_tuple:
            invalid_moves_for_king.append(down)
        if up_left in pos_tuple:
            invalid_moves_for_king.append(up_left)
        if up_right in pos_tuple:
            invalid_moves_for_king.append(up_right)
        if down_left in pos_tuple:
            invalid_moves_for_king.append(down_left)
        if down_right in pos_tuple:
            invalid_moves_for_king.append(down_right)

        return invalid_moves_for_king
    
    def is_in_check(self):
        """
        Returns True if the king is in check or False
        """

        in_check = False

        # Iterate through every position, if the king's position is included
        # in return value of get_invalid_moves_for_opposite_king() of any of the opposite color
        # piece, set in_check to True
        if self.piece_color == "white":
            for pos in pos_tuple:
                position = self.board.position_dict[pos]
                if position.piece is not None and position.piece.piece_color == "black":
                    invalid_moves = position.piece.get_invalid_moves_for_opposite_king()
                    if self.piece_position in invalid_moves:
                        in_check = True
                        break

        if self.piece_color == "black":
            for pos in pos_tuple:
                position = self.board.position_dict[pos]
                if position.piece is not None and position.piece.piece_color == "white":
                    invalid_moves = position.piece.get_invalid_moves_for_opposite_king()
                    if self.piece_position in invalid_moves:
                        in_check = True
                        break
        
        return in_check

    def is_in_mate(self):
        """
        Returns True if king is in mate else False
        """

        temp = []
        # Check if king is in check
        if not self.is_in_check():
            return False
        
        # Check if king can move to get out of check
        if self.get_moves() != []:
            return False
        
        in_mate = True
        
        # Iterate through every position, if a move of a same colored piece
        # is found such that it removes the king from check, set in_mate to False 
        if self.piece_color == "white":
            for pos in pos_tuple:
                position = self.board.position_dict[pos] # position object of the positoin 'pos'
                # If there is no piece on the position or the piece is of opposite color, continue
                if position.piece is None or position.piece.piece_color == "black":
                    continue
                # Get the moves of the piece on the position
                piece_moves = position.piece.get_moves()
                # Save the original position of the piece
                initial_position = position.piece.piece_position
                # Iterate through all the moves of the piece
                # Play them one by one and check if king is still under check
                for final_position in piece_moves:
                    # Forcecully move the piece to final_position
                    position.piece.forced_move(final_position)
                    # If after moving the piece, the king is no longer in check
                    # set in_mate = False
                    # Else undo the move made by the piece and move on to the
                    # next move of the piece
                    if not self.is_in_check():
                        temp.append(initial_position, final_position)
                        in_mate = False
                        break
                    else:
                        # Take the new position of the piece
                        new_position = self.board.position_dict[final_position]
                        # Move the piece from new_position to initial_position
                        new_position.piece.forced_move(initial_position)
                # If the king is not in mate, break the loop
                if not in_mate:
                    break
        
        if self.piece_color == "black":
            for pos in pos_tuple:
                position = self.board.position_dict[pos]
                if position.piece is None or position.piece.piece_color == "white":
                    continue
                piece_moves = position.piece.get_moves()
                initial_position = position.piece.piece_position
                for final_position in piece_moves:
                    position.piece.forced_move(final_position)
                    if not self.is_in_check():
                        temp.append(initial_position, final_position)
                        in_mate = False
                        break
                    else:
                        new_position = self.board.position_dict[final_position]
                        new_position.piece.forced_move(initial_position)
                if not in_mate:
                    break
      
        return in_mate

    def __str__(self):
        return f"{self.piece_color[0]}k"

