from square import Square


class Win_Base:
    """ Represents a base class for the winning base in the game.

    Attributes:
        list_win_square (list): The list of squares in the winning base.
        win_square (int or float): The identifier of the square where the player enters the win base.
        color (str): The color of the winning base.
    """
    def __init__(self, win_square, color):
        """ Represents a base class for the winning base in the game.

        Args:
            win_square (int or float): The identifier of the square where the player enters the win base.
            color (str): The color of the winning base.

        """

        self.id_win_square = win_square
        self.list_win_square = []
        self.color = color

    def mapping_win_base(self, x, y, size):
        """ Maps the squares in the winning base based on the color.

        Args:
            x (int or float): The x-coordinate of first square in the base.
            y (int or float): The y-coordinate of first square in the base.
            size (int or float): The size of side each square in the base.
        """
        if self.color == "green3":
            for i in range(5):
                self.list_win_square.append(Square(x + size * i, y + size, size, self.color))

        if self.color == "gold":
            for i in range(5):
                self.list_win_square.append(Square(x - size, y + size * (i + 1), size, self.color))

        if self.color == "cornflowerblue":
            for i in range(5):
                self.list_win_square.append(Square(x + size * (4 - i), y + size, size, self.color))

        if self.color == "red":
            for i in range(5):
                self.list_win_square.append(Square(x - size, y + size * (4 - i), size, self.color))
                
    def draw_win_base(self, screen, x, y, size):
        """ Draws the winning base on the screen.

        Args:
            screen: The pygame screen object.
            x (int or float): The x-coordinate of first square in the base.
            y (int or float): The y-coordinate of first square in the base.
            size (int or float): The size of side each square in the base.
        """
        if self.color == "green3":
            for i in range(5):
                self.list_win_square[i].draw_square(screen)
            Square(x + 1, y + 1, size - 2, self.color).draw_square(screen, black=False)

        if self.color == "gold":
            for i in range(5):
                self.list_win_square[i].draw_square(screen)
            Square(x + 1, y + 1 + size, size - 2, self.color).draw_square(screen, black=False)

        if self.color == "cornflowerblue":
            for i in range(5):
                self.list_win_square[i].draw_square(screen)
            Square(x + 1 + size * 4, y + 1 + 2 * size, size - 1, self.color).draw_square(screen, black=False)

        if self.color == "red":
            for i in range(5):
                self.list_win_square[i].draw_square(screen)
            Square(x + 1 - 2 * size, y + 1 + 4 * size, size - 2, self.color).draw_square(screen, black=False)

    def is_winner(self, player, i):
        """ Checks if the player's piece is in the winning base.

        Args:
            player (Player): The player whose piece is checked if is winner.
            i (int): The index of the player's piece.

        Returns:
            bool: True if the player's piece is in the winning base, False otherwise.
        """
        return player.position[i] in self.list_win_square

    def win_enter(self, player, i):
        """
        Handles the player entering the winning base.

        If the player's piece is in the starting position, it remains unchanged.
        If the target square in the winning base is unoccupied, the player's piece is moved to that square.
        If the target square is occupied, the player's piece cannot enter the winning base.

        Args:
            player (Player): The player.
            i (int): The index of the player's piece.
        """
        if player.id_position[i] == -6:
            pass
        elif len(self.list_win_square[abs(player.id_position[i])-1].occupied) == 0:
            player.position[i] = self.list_win_square[abs(player.id_position[i])-1]
            player.position[i].get_occupied(player)
        else:
            pass

    def is_all_pieces_winners(self, player):
        """
        Checks if all the player's pieces are in the winning base.

        Args:
            player (Player): The player object.

        Attributes:
            winners (int): The amount of player's winning pieces

        Returns:
            bool: True if all pieces are in the winning base, False otherwise.
       """

        winners = 0
        for i in range(4):
            if self.is_winner(player, i):
                winners += 1
        return winners == 4
