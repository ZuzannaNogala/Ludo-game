
from board import Board
from human import Human
from dice import Dice
import pygame


class Game:
    """ A class representing the Ludo game.

    Attributes:
        list_of_players (list): A list containing instances of the Human class representing the players in the game.
        amount_of_human (int): The number of human players in the game.
        board (Board): An instance of the Board class representing the game board.
        dice (Dice): An instance of the Dice class representing the game dice.
        running (bool): A boolean indicating whether the game is running or not.

    """
    def __init__(self):
        self.list_of_players = []
        self.amount_of_human = 0
        self.board = Board()
        self.dice = Dice(0, 0, 0)
        self.running = True

    def add_dice(self, x, y, n):
        """
        Add the dice to the game.

        Args:
            x (int or float): The x-coordinate of the top-left corner of the dice.
            y (int or float): The y-coordinate of the top-left corner of the dice.
            n (int): The size the dice (width and height).
        """
        self.dice = Dice(x, y, n)

    def add_human(self, col, l, leave, win, lst):
        """
        Add a human player to the game.

        Args:
            col (str): The color of the player.
            l (int): The number of squares on the path.
            leave (Square): The square where the player leaves the house.
            win (Square): The square where the player enters the win base.
            lst (list): The list of house squares.
        """
        human = Human(col, l)
        human.set_start_position(lst)
        self.list_of_players.append(human)
        human.leave_square = leave
        human.win_square = win
        self.amount_of_human += 1

    def change_position(self, player, j, i, value):
        """Change the position of a player on the board.

        Args:
            player (Player): The player to move.
            j (int): The index of the current player.
            i (int): The index of the player's piece.
            value (int): The dice value.

        Returns:
            int: None or the new index of the current player in the list.
        """
        prev_square = player.position[i]
        player.position[i].get_release(player)
        if prev_square not in player.home and not self.board.list_win_base[j].is_winner(player, i):
            prev_id = player.id_position[i]
            piece_move = player.go(i, value)
            if piece_move >= 0:
                player.position[i] = self.board.id_square[piece_move]
                player.position[i].get_occupied(player)
            else:
                self.board.list_win_base[j].win_enter(player, i)  # ogarnac to pole
                if prev_square == player.position[i] or player.position[i] == -6:
                    player.position[i].get_occupied(player)
                    j = self.change_current_player(j - 1)
                    current_player = self.list_of_players[j]
                    player.id_position[i] = prev_id  # ziu
                    return j
        elif prev_square in player.home:
            player.position[i] = self.board.id_square[player.leave_house(i)]
            player.position[i].get_occupied(player)

    def move(self, current_player, value, j):
        """
        Move a player on the board.

        Args:
            current_player (Player): The current player.
            value (int): The dice value.
            j (int): The index of the current player in the list of players.

        Returns:
            tuple: The updated current player, index, and dice value.
       """
        if current_player.get_player_mouse(0):
            if self.board.list_win_base[j].is_winner(current_player, 0) or \
                    (value != 6 and current_player.position[0] == current_player.home[0]):
                pass
            else:
                a = self.change_position(current_player, j, 0, value)
                self.check_kill(current_player, 0)
                if a is None:
                    if value != 6:
                        j = self.change_current_player(j)
                        current_player = self.list_of_players[j]
                    else:
                        value = None
                    return current_player, j, value
                else:
                    current_player = self.list_of_players[a]
                    return current_player, a, value
        if current_player.get_player_mouse(1):
            if self.board.list_win_base[j].is_winner(current_player, 1) or \
                    (value != 6 and current_player.position[1] == current_player.home[1]):
                pass
            else:
                a = self.change_position(current_player, j, 1, value)
                self.check_kill(current_player, 1)
                if a is None:  # dodatkowy rzut
                    if value != 6:
                        j = self.change_current_player(j)
                        current_player = self.list_of_players[j]
                    else:
                        value = None
                    return current_player, j, value
                else:
                    current_player = self.list_of_players[a]
                    return current_player, a, value
        if current_player.get_player_mouse(2):
            if self.board.list_win_base[j].is_winner(current_player, 2) or \
                    (value != 6 and current_player.position[2] == current_player.home[2]):
                pass
            else:
                a = self.change_position(current_player, j, 2, value)
                self.check_kill(current_player, 2)
                if a is None:
                    if value != 6:
                        j = self.change_current_player(j)
                        current_player = self.list_of_players[j]
                    else:
                        value = None
                    return current_player, j, value
                else:
                    current_player = self.list_of_players[a]
                    return current_player, a, value
        if current_player.get_player_mouse(3) and not self.board.list_win_base[j].is_winner(current_player, 3):
            if self.board.list_win_base[j].is_winner(current_player, 3) or \
                    (value != 6 and current_player.position[3] == current_player.home[3]):
                pass
            else:
                a = self.change_position(current_player, j, 3, value)
                self.check_kill(current_player, 3)
                if a is None:
                    if value != 6:
                        j = self.change_current_player(j)
                        current_player = self.list_of_players[j]
                    else:
                        value = None
                    return current_player, j, value
                else:
                    current_player = self.list_of_players[a]
                    return current_player, a, value

        return current_player, j, value

    def is_available_pieces(self, current_player, j, value):
        """
        Check if there are any available pieces for the current player to move.

        Args:
            current_player (Player): The current player.
            j (int): The index of the current player in the list of players.
            value (int): The dice value.

        Returns:
            int: The number of available pieces.
        """
        available = 4
        notwinners = []
        for index in range(4):
            if self.board.list_win_base[j].is_winner(current_player, index) or (
                    current_player.position[index] == current_player.home[index] and value != 6):
                available -= 1
            if not self.board.list_win_base[j].is_winner(current_player, index) and current_player.position[index] != current_player.home[index]:
                notwinners.append(index)
        if len(notwinners) != 0:
            i = 0
            while value is not None and i < len(notwinners):
                if current_player.l - 7 <= current_player.id_position[notwinners[i]] <= current_player.l - 2:
                    k = current_player.id_position[notwinners[i]] + value
                    if k >= current_player.l - 2:
                        k = current_player.l - 2 - k + 1
                        if abs(k) < 5:
                            if len(self.board.list_win_base[j].list_win_square[abs(k)].occupied) != 0:
                                available -= 1
                        elif abs(k) >= 5:
                            available -= 1
                i += 1
        return available

    def check_kill(self, current_player, i):
        """
        Check if any opponent's pieces can be killed by current position.

        Args:
            current_player (Player): The current player.
            i (int): The index of the current player's piece.

        """
        if len(self.board.id_square[current_player.id_position[i]].occupied) > 1 and \
                not self.board.id_square[current_player.id_position[i]].is_special():
            for player in self.board.id_square[current_player.id_position[i]].occupied:
                if player.color != current_player.color:
                    for index in range(len(player.id_position)):
                        if player.id_position[index] == current_player.id_position[i]:
                            player.get_killed(index)

    @staticmethod
    def change_current_player(j):
        """
        Change the current player index to the next player.

        Args:
            j (int): The index of the current player in the list of players.

        Returns:
            int: The index of the next player.
        """
        if j <= 2:
            j += 1
        else:
            j = 0
        return j

    def mapping_game(self):
        """
        Map the squares, houses, and win bases on the board.
        """
        self.board.mapping(35, 210 + 35, 35, "LEFT")
        self.board.mapping(314 - 2 * 35, 36.5, 35, "TOP")
        self.board.mapping(346, 245, 35, "RIGHT")
        self.board.mapping(314, 350, 35, "BOTTOM")

        for i in [3, 8, 16, 21, 29, 34, 42, 47]:
            self.board.id_square[i].get_special()

        self.board.mapping_house(60, 59.65)
        self.board.mapping_house(385, 59.65)
        self.board.mapping_house(385, 380.65)
        self.board.mapping_house(60, 380.65)

        self.board.add_win_base(70, 245, 35, 6, "green3")
        self.board.add_win_base(314, 36.5, 35, 19, "gold")
        self.board.add_win_base(346, 245, 35, 32, "cornflowerblue")
        self.board.add_win_base(314, 350, 35, 45, "red")

    def game(self):
        """
        The game loop.

        Attributes:
            colors (dict):
            i (int): The index of the player's piece.
            j (int): The index of current player in the list of player.
            f (int): The variable to informs about status of dice (if dice was rolled f changes, otherwise not)
            v (int): The value of the dice roll.
            prev_f (int): Previous status of f.
        """

        colors = {"darkgreen": "GREEN", "goldenrod": "YELLOW", "cyan4": "BLUE", "brown4": "RED"}
        self.mapping_game()
        self.add_dice(550, 550, 40)
        self.add_human("darkgreen", 8, self.board.id_square[8], self.board.id_square[6], self.board.id_house[0:4])
        self.add_human("goldenrod", 21, self.board.id_square[21], self.board.id_square[19], self.board.id_house[4:8])
        self.add_human("cyan4", 34, self.board.id_square[34], self.board.id_square[32], self.board.id_house[8:12])
        self.add_human("brown4", 47, self.board.id_square[47], self.board.id_square[45], self.board.id_house[12:16])

        pygame.display.set_caption("Ludo")
        pygame.init()
        pygame.font.init()
        i, j, f = 0, 0, 0
        current_player = self.list_of_players[j]
        v = None
        prev_f = f

        while self.running:
            self.board.draw(self.list_of_players)
            if j < 2:
                self.board.draw_turn(current_player.color, current_player.home[0].x - 28, current_player.home[0].y - 28,
                                     p="UP")
                self.dice.draw_empty_dice(self.board.screen)
            else:
                self.board.draw_turn(current_player.color, current_player.home[0].x - 28, current_player.home[0].y - 28,
                                     p="DOWN")
                self.dice.draw_empty_dice(self.board.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.dice.get_dice_mouse():
                        if prev_f == f:
                            v = self.dice.roll()
                            f += 1
                    if self.is_available_pieces(current_player, j, v) == 0 and self.dice.get_dice_mouse():
                        prev_j = j
                        j = self.change_current_player(j)
                        current_player = self.list_of_players[j]
                        if prev_j != j:
                            prev_f = f
                            self.dice.draw_dice_value(self.board.screen, v)
                        v = None
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        prev_j = j
                        if v is not None:
                            current_player, j, v = self.move(current_player, v, j)
                            if v is None:
                                prev_f = f
                            if prev_j != j:
                                prev_f = f
                                v = None

                for i in range(4):
                    if self.board.list_win_base[i].is_all_pieces_winners(self.list_of_players[i]):
                        print(f"Congratulation, {colors[self.list_of_players[i].color]} is winner!!!")
                        self.running = False

            if v is not None:
                self.dice.draw_dice_value(self.board.screen, v)

            pygame.display.update()
            self.board.clock.tick(60)


if __name__ == "__main__":
    Game().game()