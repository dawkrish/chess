from .vars import position_color_relation

class Position:
    """
    Creates a position object with given code, generates the position color automatically
    """

    def __init__(self, code):
        """
        code: code of the position on board
        """

        self.position_code = code.lower()
        self.position_color = position_color_relation[code]
        self.piece = None
    
    def __str__(self):
        return self.position_code +" " + self.position_color