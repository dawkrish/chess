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
                    invalid_moves.extend(piece_at_pos.get_moves_for_king())

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
                    invalid_moves.extend(piece_at_pos.get_moves_for_king())

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

    def get_moves_for_king(self):
        return []

    def __str__(self):
        return f"{self.piece_color[0]}k"

