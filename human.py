from player import Player


class Human(Player):
    """ Represents a human player in the game.

    Attributes:
        Inherits attributes from the Player class.
    """

    def go(self, i, value=0):
        """ Moves the player's piece on the board, change the identifier of square which was occupied by the player's piece

        Args:
            i (int): The index of the player's piece.
            value (int, optional): The dice roll result, the number of steps to move. Defaults to 0.

        Returns:
            int: The updated position of the player's piece.
        """

        if not self.is_piece_in_home(i):
            if self.id_position[i] >= 0 and self.id_position[i] + value <= 51:
                for index in range(value):
                    self.id_position[i] += 1
                    if self.id_position[i] == self.l - 1:
                        self.id_position[i] = -1
                        for index2 in range(index, value - 1):
                            self.id_position[i] -= 1
                        return self.id_position[i]
                return self.id_position[i]
            elif self.id_position[i] >= 0:
                self.id_position[i] = self.id_position[i] - 52
                for index in range(value):
                    self.id_position[i] += 1
                    if self.id_position[i] == self.l - 1:
                        self.id_position[i] = -1
                        for index2 in range(index, value - 1):
                            self.id_position[i] -= 1
                        return self.id_position[i]
                return self.id_position[i]

    def get_killed(self, i):
        """ Handles the event when the player's piece gets killed.

        Args:
            i (int): The index of the killed piece.
        """
        self.come_back(i)

    def come_back(self, i):
        """ Moves the player's piece back to the home square.

        Args:
            i (int): The index of the player's piece.
        """
        self.position[i].get_release(self)
        self.position[i] = self.home[i]
        self.id_position[i] = self.l
        self.position[i].get_occupied(self)

    def leave_house(self, i):
        """ Moves the player's piece out of the house.

        Args:
            i (int): The index of the player's piece.

        Returns:
            int: The updated position of the player's piece.
        """
        self.position[i] = self.leave_square
        return self.id_position[i]
