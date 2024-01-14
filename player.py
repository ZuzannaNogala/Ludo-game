from square import Square
import pygame


class Player:
    """ Represents a player in the game.

    Attributes:
        col (str): The color of the player.
        l (int): The identifier of leave square for the player on the board.
        leave_square (Square, optional): The square from which the player leaves the house. Defaults to Square(0, 0, 0).
        win_square (Square, optional): The square where the player enters the win base. Defaults to Square(0, 0, 0).
        home (list): List of House's Squares
        position (list): List of four Squares which are occupied by player
        id_position (list): List of four identifiers of squares which are occupied by player. At first all elements are l.
    """
    def __init__(self, col, l, leave_square = Square(0,0,0), win_square = Square(0,0,0)):

        """ Represents a player in the game.

        Args:
            col (str): The color of the player.
            l (int): The identifier of leave square for the player on the board.
            leave_square (Square, optional): The square from which the player leaves the house. Defaults to Square(0, 0, 0).
            win_square (Square, optional): The square where the player enters the win base. Defaults to Square(0, 0, 0).

        """

        self.position = []
        self.id_position = [l for _ in range(4)]
        self.l = l
        self.home = []
        self.leave_square = Square(leave_square.x, leave_square.y, 35)
        self.win_square = Square(win_square.x, win_square.y, 35)
        self.color = col

    def set_start_position(self, lst):
        """ Sets the start position for the player.

        Args:
            lst (list): The list of squares representing the start position.
        """

        self.position = [i for i in lst]
        self.home = [i for i in lst]
        for square in self.home:
            square.get_occupied(self)

    def is_piece_in_home(self, i):
        """ Checks if the player's piece is in the home square.

        Args:
            i (int): The index of the player's piece.

        Returns:
            bool: True if the player's piece is in the home square, False otherwise.
        """

        return self in self.home[i].occupied

    def get_player_mouse(self, i):
        """ Checks if the user's mouse  is within the boundaries of a square of player's piece.

        Args:
            i (int): The index of the player's piece.

        Attributes:
            x , y (tuple[int, int]): The position of user's mouse to check.

        Returns:
            bool: True if the player's piece is within the square, False otherwise.
        """

        x, y = pygame.mouse.get_pos()
        return self.position[i].x + self.position[i].size >= x >= self.position[i].x and self.position[i].y + self.position[i].size >= y >= self.position[i].y

    def draw_player(self, screen, square):
        """ Draws the player's piece on the screen.

        Args:
            screen: The screen to draw on.
            square (Square): The square representing the player's position.
        """

        pygame.draw.circle(screen, self.color, (square.x + square.size/2, square.y + square.size/2), 10)

