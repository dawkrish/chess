from .vars import pos_tuple
from .position import Position
from .pieces.pawn import Pawn
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.knight import Knight
from .pieces.bishop import Bishop
from .pieces.rook import Rook


class Board:
    """
    Creates a board object
    """

    # Pawn positions
    white_pawn_positions = ("a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2")
    black_pawn_positions = ("a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7")
    # Knight Positions
    white_knight_positions = ("b1", "g1")
    black_knight_positions = ("b8", "g8")
    # Bishop Positions
    white_bishop_positions = ("c1", "f1")
    black_bishop_positions = ("c8", "f8")
    # Rook Positions
    white_rook_positions = ("a1", "h1")
    black_rook_positions = ("a8", "h8")
    # Queen Positions
    white_queen_positions = ("d1",)
    black_queen_positions = ("d8",)
    # King Positions
    white_king_positions = ("e1",)
    black_king_positions = ("e8",)
    
    def __init__(self):
        self.position_dict = {}
        # Creating Positions
        for pos in pos_tuple:
            self.position_dict[pos] = Position(pos)

        # Creating Pawns
        for pos in Board.white_pawn_positions:
            piece = Pawn(self, "white", pos)
            self.position_dict[pos].piece = piece
        for pos in Board.black_pawn_positions:
            piece = Pawn(self, "black", pos)
            self.position_dict[pos].piece = piece
        
        # Creating Bishops
        for pos in Board.white_bishop_positions:
            piece = Bishop(self, "white", pos)
            self.position_dict[pos].piece = piece
        for pos in Board.black_bishop_positions:
            piece = Bishop(self, "black", pos)
            self.position_dict[pos].piece = piece
        
        # Creating Rooks
        for pos in Board.white_rook_positions:
            piece = Rook(self, "white", pos)
            self.position_dict[pos].piece = piece
        for pos in Board.black_rook_positions:
            piece = Rook(self, "black", pos)
            self.position_dict[pos].piece = piece
        
        # Creating Queens
        for pos in Board.white_queen_positions:
            piece = Queen(self, "white", pos)
            self.position_dict[pos].piece = piece
        for pos in Board.black_queen_positions:
            piece = Queen(self, "black", pos)
            self.position_dict[pos].piece = piece
        
        # Creating Kings    
        for pos in Board.white_king_positions:
            piece = King(self,"white", pos)
            self.position_dict[pos].piece = piece
        for pos in Board.black_king_positions:
            piece = King(self,"black", pos)
            self.position_dict[pos].piece = piece
        
        # Creating Knights
        for pos in Board.white_knight_positions:
            piece = Knight(self, "white", pos)
            self.position_dict[pos].piece = piece
        for pos in Board.black_knight_positions:
            piece = Knight(self,"black", pos)
            self.position_dict[pos].piece = piece
            

    def print_board(self):
        '''
        Prints the chess board on terminal
        '''

        print("   -" + ("-----" * 8))
        print("   |", "Chess Board".center(39), "|", sep="")
        for i in range(8, 0, -1):
            print("   -" + ("-----" * 8))
            print(f" {i} ", end="")
            for j in range(97, 105):
                pos = self.position_dict[f"{chr(j)}{i}"]
                if pos.piece is None:
                    res = "  "
                else:
                    res = str(pos.piece)
                print("| " + res, end = " ")
            print("|")
        print("   -" + ("-----" * 8))
        print(end="   ")
        for i in range(97, 105):
            print(f"{chr(i)}".center(5), end="")
        print()

b = Board()
b.print_board()


