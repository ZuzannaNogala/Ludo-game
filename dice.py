import random
import pygame


class Dice:
    """ Represents the dice object.

    Attributes:
        x (int or float): The x-coordinate of the top-left corner of the dice.
        y (int or float): The y-coordinate of the top-left corner of the dice.
        n (int or float): The size the dice (width and height).
        value (int): The current value shown on the dice.
        pos (tuple): The position of the dice on the board.
    """
    def __init__(self, x, y, n):
        """
        Represents the dice object.

        Args:
            x (int or float): The x-coordinate of the top-left corner of the dice.
            y (int or float): The y-coordinate of the top-left corner of the dice.
            n (int or float): The size the dice (width and height).

        """
        self.value = 0
        self.x = x
        self.y = y
        self.pos = x, y
        self.size = n

    def roll(self):
        """
        Rolls the dice and returns the new value.

        Returns:
            int: The new value rolled on the dice.
        """
        self.value = random.randint(1, 6)
        return self.value

    def get_dice_mouse(self):
        """
        Checks if the user's mouse is over the dice.

        Returns:
            bool: True if the mouse is over the dice, False otherwise.
        """
        x, y = pygame.mouse.get_pos()
        return self.x + self.size >= x >= self.x and self.y + self.size >= y >= self.y

    def draw_empty_dice(self, screen):
        """
        Draws an empty dice (without the value) on the screen.

        Args:
            screen: The pygame screen to draw on.
        """
        pygame.draw.rect(screen, "white", pygame.Rect(self.x, self.y, self.size, self.size))
        
    def draw_dice_value(self, screen, value):
        """
        Draws the dice with a rolled value on the screen.

        Args:
            screen: The pygame screen to draw on.
            value (int): The value to be displayed on the dice.
        """
        if value == 1:
            pygame.draw.circle(screen, "black", (self.x + self.size/2, self.y + self.size/2), 5)
        elif value == 2:
            pygame.draw.circle(screen, "black", (self.x + self.size/4, self.y + self.size/4), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2 + 10, self.x + self.size/2 + 10), 5)
        elif value == 3:
            pygame.draw.circle(screen, "black", (self.x + self.size/4, self.y + self.size/4), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2, self.y + self.size/2), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2 + 10, self.x + self.size/2 + 10), 5)
        elif value == 4:
            pygame.draw.circle(screen, "black", (self.x + self.size/4, self.y + self.size/4), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/4, self.y + self.size/2 + 10), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2 + 10, self.x + self.size/2 + 10), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2 + 10, self.y + self.size/4), 5)
        elif value == 5:
            pygame.draw.circle(screen, "black", (self.x + self.size/4, self.y + self.size/4), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/4, self.y + self.size/2 + 10), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2 + 10, self.x + self.size/2 + 10), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2 + 10, self.y + self.size/4), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2, self.y + self.size/2), 5)
        elif value == 6:
            pygame.draw.circle(screen, "black", (self.x + self.size/4, self.y + 10), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/4, self.y + self.size/2 + 10), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2 + 10, self.x + self.size/2 + 10), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2 + 10, self.y + self.size/4), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/4, self.y + self.size/2), 5)
            pygame.draw.circle(screen, "black", (self.x + self.size/2 + 10, self.y + self.size/2), 5)

