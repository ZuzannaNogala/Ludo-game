import pygame

from win_basa import Win_Base
from dice import Dice
from square import Square

ludo_dice = Dice(550, 550, 40)


class Board:
    """
    Represents a Ludo board.

    Attributes:
        screen (pygame.Surface): The game screen where the game is displayed.
        clock (pygame.time.Clock): The game clock.
        id_square (list): A list of Square objects representing the squares on the board.
        id_house (list): A list of Square objects representing the player houses on the board.
        list_win_base (list): A list of Win_Base objects representing the win bases on the board.
        col (list): A list of colors for the players.
    """

    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.id_square = []
        self.id_house = []
        self.list_win_base = []
        self.col = ["darkgreen", "goldenrod", "cyan4", "brown4"]

    def add_win_base(self, x, y, size, win_square, color):
        """
        Adds a win base to the board.

        Args:
            x (int): The x-coordinate of the first square in win base.
            y (int): The x-coordinate of the first square in win base.
            size (int): The size of square's side in the win base.
            win_square (Square): The Square object representing the win square.
            color (str): The color of the win base.
        """
        win_base = Win_Base(win_square, color)
        win_base.mapping_win_base(x, y, size)
        self.list_win_base.append(win_base)

    def draw_path(self, p):
        """
        Draws a path on the board.

        Args:
            p (str): The direction of the path. Possible values: "LEFT", "TOP", "RIGHT", "BOTTOM".
        """
        if p == "LEFT":
            for i in range(6):
                self.id_square[i].draw_square(self.screen)
            self.id_square[6].draw_square(self.screen)
            for i in range(7, 13):
                self.id_square[i].draw_square(self.screen)

        if p == "TOP":
            for i in range(13, 19):
                self.id_square[i].draw_square(self.screen)
            self.id_square[19].draw_square(self.screen)
            for i in range(20, 26):
                self.id_square[i].draw_square(self.screen)

        if p == "RIGHT":
            for i in range(26, 32):
                self.id_square[i].draw_square(self.screen)
            self.id_square[32].draw_square(self.screen)
            for i in range(33, 39):
                self.id_square[i].draw_square(self.screen)

        if p == "BOTTOM":
            for i in range(39, 45):
                self.id_square[i].draw_square(self.screen)
            self.id_square[45].draw_square(self.screen)
            for i in range(46, 52):
                self.id_square[i].draw_square(self.screen)

    def mapping(self, x, y, m, p):
        """
        Maps the squares on the board.

        Args:
            x (int or float): The x-coordinate of the starting point.
            y (int or float): The y-coordinate of the starting point.
            m (int or float): The size of each square's side.
            p (str): The orientation of the mapping. Possible values: "LEFT", "TOP", "RIGHT", "BOTTOM".
        """
        if p == "LEFT":
            for i in range(6):
                self.id_square.append(Square(x + 1 + m * (5 - i), y + 2 * m + 1, m - 2))
            self.id_square.append(Square(x + 1, y + m + 1, m - 2))
            for i in range(6):
                self.id_square.append(Square(x + 1 + m * i, y + 1, m - 2))

        if p == "RIGHT":
            for i in range(6):
                self.id_square.append(Square(x + 1 + m * i, y + 1, m - 2))
            self.id_square.append(Square(x + m * i + 1, y + m + 1, m - 2))
            for i in range(6):
                self.id_square.append(Square(x + 1 + m * (5 - i), y + 2 * m + 1, m - 2))

        if p == "TOP":
            for i in range(6):
                self.id_square.append(Square(x + 1, y + 1 + m * (5 - i), m - 2))
            self.id_square.append(Square(x + m + 1, y + 1, m - 2))
            for i in range(6):
                self.id_square.append(Square(x + 2 * m + 1, y + 1 + m * i, m - 2))

        if p == "BOTTOM":
            for i in range(6):
                self.id_square.append(Square(x + 1, y + 1 + m * i, m - 2))
            self.id_square.append(Square(x - m + 1, y + i * m + 1, m - 2))
            for i in range(6):
                self.id_square.append(Square(x - 2 * m + 1, y + 1 + m * (5 - i), m - 2))

    def draw_house(self, color, x, y):
        """
        Draws a player house on the board.

        Args:
            color (str): The color of the house.
            x (int or float): The x-coordinate of the house.
            y (int or float): The y-coordinate of the house.
        """
        pygame.draw.rect(self.screen, "White", pygame.Rect(x, y, 150, 150))
        pygame.draw.rect(self.screen, color, pygame.Rect(x + 2.5, y + 2.5, 145, 145))
        pygame.draw.circle(self.screen, "white", (x + 40, y + 40), 22)
        self.id_house[-1].draw_square(self.screen, False)
        pygame.draw.circle(self.screen, "white", (x + 110, y + 40), 22)
        self.id_house[-1].draw_square(self.screen, False)
        pygame.draw.circle(self.screen, "white", (x + 110, y + 110), 22)
        self.id_house[-1].draw_square(self.screen, False)
        pygame.draw.circle(self.screen, "white", (x + 40, y + 110), 22)
        self.id_house[-1].draw_square(self.screen, False)

    def draw_turn(self, color, x, y, p):
        """
        Draws the turn indicator on the board.

        Args:
            color (str): The color of the player who is the current player.
            x (int or float): The x-coordinate of the top-left corner of rectangle where text is displayed.
            y (int or float): The y-coordinate of the top-left corner of rectangle where text is displayed.
            p (str): The position of the rectangle where text is displayed. Possible values: "UP", "DOWN".
        """
        font = pygame.font.Font(None, 20)
        if p == "UP":
            pygame.draw.rect(self.screen, color, pygame.Rect(x + 2.5 + 145/4, y + 2.5 - 145/3 + 10, 145/2, 20))
            text = font.render("YOUR TURN", True, "black")
            text_rect = text.get_rect(center=pygame.Rect(x + 2.5 + 145/4, y + 2.5 - 145/3 + 10, 145/2, 20).center)
        if p == "DOWN":
            pygame.draw.rect(self.screen, color, pygame.Rect(x + 2.5 + 145 / 4, y + 145 + 20 , 145 / 2, 20))
            text = font.render("YOUR TURN", True, "black")
            text_rect = text.get_rect(center=pygame.Rect(x + 2.5 + 145 / 4, y + 145 + 20 , 145 / 2, 20).center)
        self.screen.blit(text, text_rect)

    def mapping_house(self, x, y):
        """
        Maps the player houses on the board.

        Args:
            x (float or int): The x-coordinate of the starting point.
            y (float or int): The y-coordinate of the starting point.
        """
        self.id_house.append(Square(x + 28, y + 28, 25))
        self.id_house.append(Square(x + 98, y + 28, 25))
        self.id_house.append(Square(x + 98, y + 98, 25))
        self.id_house.append(Square(x + 28, y + 98, 25))

    def draw(self, list_of_player):
        """
        Draws the Ludo board.

        Args:
            list_of_player (list): A list of Player who participate in game.
        """
        self.screen.fill("Grey")

        self.draw_house("green3", 60, 59.65)
        self.draw_house("gold", 385, 59.65)
        self.draw_house("cornflowerblue", 385, 380.65)
        self.draw_house("red", 60, 380.65)

        self.draw_path("LEFT")
        self.list_win_base[0].draw_win_base(self.screen, 70, 245, 35)

        self.draw_path("TOP")
        self.list_win_base[1].draw_win_base(self.screen, 314, 36.5, 35)

        self.draw_path("RIGHT")
        self.list_win_base[2].draw_win_base(self.screen, 346, 245, 35)

        self.draw_path("BOTTOM")
        self.list_win_base[3].draw_win_base(self.screen, 314, 350, 35)

        ludo_dice.draw_empty_dice(self.screen)

        for player in list_of_player:
            for i in range(4):
                player.draw_player(self.screen, player.position[i])
