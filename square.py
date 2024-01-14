import pygame


class Square:
    """ Represents a square on the game board.

    Attributes:
        x (int or float): The x-coordinate of the square.
        y (int or float): The y-coordinate of the square.
        size (int or float): The length of side of the square.
        col (str, optional): The color of the square. Defaults to "White".
        special (bool, optional): Indicates if the square is special. Defaults to False.
        occupied (list): The list of players who occupies the square
    """
    def __init__(self, x, y, size, col="White", special=False):
        """ Represents a square on the game board.

        Args:
            x (int or float): The x-coordinate of the square.
            y (int or float): The y-coordinate of the square.
            size (int or float): The length of side of the square.
            col (str, optional): The color of the square. Defaults to "White".
            special (bool, optional): Indicates if the square is special. Defaults to False.

        """

        self.x = x
        self.y = y
        self.position = x, y
        self.size = size
        self.color = col
        self.occupied = []
        self.special = special

    def get_occupied(self, player):
        """ Gets occupied square by the player

        Args:
            player (Player): The player to add to the list of occupied players.
        """

        self.occupied.append(player)

    def get_square_mouse(self, position):
        """ Checks if the given position by user's mouse is within the boundaries of the square.

        Args:
            position (tuple[int, int]): The position to check.

        Returns:
            bool: True if the position is within the boundaries of the square, False otherwise.
        """

        x, y = position
        return self.x + self.size / 2 >= x >= self.x and self.y + self.size / 2 >= y >= self.y

    def get_release(self, player):
        """ Removes the player from the list of occupied players.

        Args:
            player (Player): Removes the player from the list of occupied squares.
        """

        a = 0
        while a < len(self.occupied) and self.occupied[a] == player:
            a += 1
        if a > 0:
            self.occupied.pop(a - 1)
        elif a == 0:
            self.occupied.pop()

    def is_special(self):
        """ Checks if the square is special.

        Returns:
            bool: True if the square is special, False otherwise.
        """

        return self.special

    def get_special(self):
        """ Sets the square as special.
        """
        self.special = True

    def draw_square(self, screen, black=True):
        """ Draws the square on the screen.

        Args:
            screen: The Pygame screen to draw on.
            black (bool, optional): Indicates if the square should be drawn with a black border. Defaults to True.
        """
        if black:
            pygame.draw.rect(screen, "Black", pygame.Rect(self.x - 1, self.y - 1, self.size + 2, self.size + 2))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
        if self.special:
            pygame.draw.rect(screen, "Black", pygame.Rect(self.x + 1.5, self.y + 1.5, self.size - 4, self.size - 4))
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x + 2.5, self.y + 2.5, self.size - 6, self.size - 6))
