import unittest
from unittest.mock import patch
import pygame
from dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.dice = Dice(100, 100, 50)

    def tearDown(self):
        pygame.quit()

    def test_roll(self):
        with patch('random.randint', return_value=4):
            self.assertEqual(self.dice.roll(), 4)

    def test_get_dice_mouse(self):
        pygame.mouse.get_pos = lambda: (110, 110)
        self.assertTrue(self.dice.get_dice_mouse())

        pygame.mouse.get_pos = lambda: (90, 90)
        self.assertFalse(self.dice.get_dice_mouse())

    def test_draw_empty_dice(self):
        self.dice.draw_empty_dice(self.screen)

    def test_draw_dice_value(self):
        self.dice.draw_dice_value(self.screen, 3)


if __name__ == '__main__':
    unittest.main()






