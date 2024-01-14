import unittest
from square import Square
from human import Human


class TestHuman(unittest.TestCase):
    def setUp(self):
        self.home = [Square(60 + 28, 59.65 + 28, 25), Square(60 + 98, 59.65 + 28, 25), Square(60 + 98, 59.65 + 98, 25), Square(60 + 28, 59.65 + 98, 25)]
        self.player_position = [Square(0, 0, 25), Square(2, 4, 25), Square(5, 8, 25), Square(44, 12, 25)]
        self.leave_square = Square(71, 246, 35)
        self.win_square = Square(36, 281, 35)
        self.player = Human("Red", 8, leave_square=self.leave_square, win_square=self.win_square)
        self.player.set_start_position(self.home)

    def test_go_leave(self):
        self.player.id_position = [8, 8, 8, 8]
        result = self.player.go(0, 6)
        self.assertEqual(result, None)

    def test_go_on_board(self):
        self.home[1].get_release(self.player)
        self.player.id_position = [8, 21, 30, 7]
        result = self.player.go(1, 4)
        self.assertEqual(result, 25)

    def test_get_killed(self):
        self.player.position = [Square(2, 5, 25), Square(3, 8, 25), Square(10, 73, 25), Square(44, 12, 25)]
        self.player.position[2].get_occupied(self.player)
        self.player.get_killed(2)
        self.assertEqual(self.player.position[2], self.player.home[2])
        self.assertEqual(self.player.id_position[2], self.player.l)

    def test_come_back(self):
        for squares in self.player_position:
            squares.get_occupied(self.player)
        self.player_position[3].get_release(self.player)
        self.player_position[3] = self.player.home[3]
        self.player.id_position[3] = self.player.l
        self.player.come_back(3)
        self.assertEqual(self.player_position[3], self.player.home[3])
        self.assertEqual(self.player.id_position[3], self.player.l)
        self.assertIsInstance(self.player_position[3], Square)
        self.assertIn(self.player, self.player_position[3].occupied)

    def test_leave_house(self):
        self.player_position[0] = self.leave_square
        result = self.player.leave_house(0)
        self.assertEqual(result, self.player.l)
        self.assertEqual(self.player_position[0], self.leave_square)


if __name__ == '__main__':
    unittest.main()
