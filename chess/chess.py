class Position:
    """This class represents a position on a chessboard."""

    def __init__(self, board, x, y):
        """
        Defines a board position by its coordinates,
        and the board it exists on.
        :param board: Board
        :param x: int
        :param y: int
        """
        self.board = board
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Returns a string that represents a position
        by its whole Cartesian coordinates.
        :return: str
        """
        return repr((self.x, self.y))


class Board:
    """This class represents a chess board."""

    def __init__(self, chess_set, players):
        """
        Defines the board with a particular configuration.
        :param chess_set: ChessSet
        :param players: 3
        """
        if players == 2:
            self.positions = []
        elif players == 3:
            self.positions = []
        else:
            self.positions = []
        self.chess_set = chess_set


class ChessSet:
    """Represents a complete set of chess pieces. (only of one color)"""

    def __init__(self, board, pieces):
        """
        Links a chess set to a particular board
        and to the pieces of which it consists.
        :param board: Board
        :param pieces: list
        """
        self.board = board
        self.pieces = pieces[:]


class Piece:
    """Represents a chess piece. It is of some color and has a position."""

    def __init__(self, chess_set, color, position):
        """
        Defines the color, chess set, and the position of the piece.
        :param chess_set: ChessSet
        :param color: str
        :param position: Position
        """
        self.chess_set = chess_set
        self.position = position
        self.color = color

    def move(self, direction):
        """Base method for a legal piece move."""
        pass


class King(Piece):
    """Represent a king, one of the chess pieces."""

    def __init__(self, chess_set, color, position):
        """
        Defines the color, chess set, and the position of the king.
        :param chess_set: ChessSet
        :param color: str
        :param position: Position
        """
        super().__init__(chess_set, color, position)
        self.shape = "King"

    def move(self, direction):
        """Not implemented yet. The move pattern for a king."""
        pass


class Queen(Piece):
    """Represent a queen, one of the chess pieces."""

    def __init__(self, chess_set, color, position):
        """
        Defines the color, chess set, and the position of the queen.
        :param chess_set: ChessSet
        :param color: str
        :param position: Position
        """
        super().__init__(chess_set, color, position)
        self.shape = "Queen"

    def move(self, direction):
        """Not implemented yet. The move pattern for a queen."""
        pass


class Bishop(Piece):
    """Represent a bishop, one of the chess pieces."""

    def __init__(self, chess_set, color, position):
        """
        Defines the color, chess set, and the position of the bishop.
        :param chess_set: ChessSet
        :param color: str
        :param position: Position
        """
        super().__init__(chess_set, color, position)
        self.shape = "Bishop"

    def move(self, direction):
        """Not implemented yet. The move pattern for a bishop."""
        pass


class Rook(Piece):
    """Represent a rook, one of the chess pieces."""

    def __init__(self, chess_set, color, position):
        """
        Defines the color, chess set, and the position of the rook.
        :param chess_set: ChessSet
        :param color: str
        :param position: Position
        """
        super().__init__(chess_set, color, position)
        self.shape = "Rook"

    def move(self, direction):
        """Not implemented yet. The move pattern for a rook."""
        pass


class Knight(Piece):
    """Represent a knight, one of the chess pieces."""

    def __init__(self, chess_set, color, position):
        """
        Defines the color, chess set, and the position of the knight.
        :param chess_set: ChessSet
        :param color: str
        :param position: Position
        """
        super().__init__(chess_set, color, position)
        self.shape = "Knight"

    def move(self, direction):
        """Not implemented yet. The move pattern for a knight."""
        pass


class Pawn(Piece):
    """Represent a pawn, one of the chess pieces."""

    def __init__(self, chess_set, color, position):
        """
        Defines the color, chess set, and the position of the pawn.
        :param chess_set: ChessSet
        :param color: str
        :param position: Position
        """
        super().__init__(chess_set, color, position)
        self.shape = "Pawn"

    def move(self, direction):
        """Not implemented yet. The move pattern for a pawn."""
        pass
