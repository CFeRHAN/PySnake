import unittest
from unittest.mock import patch
from io import StringIO
import sys
import pygame
from snake_game import SNAKE, FRUIT, MAIN

class SnakeGameTestCase(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_snake_initialization(self):
        snake = SNAKE()
        self.assertEqual(len(snake.body), 3)
        self.assertEqual(snake.direction, pygame.math.Vector2(0, 0))
        self.assertFalse(snake.new_block)

    def test_fruit_initialization(self):
        fruit = FRUIT()
        self.assertIsInstance(fruit.pos, pygame.math.Vector2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_game_over(self, mock_stdout):
        main_game = MAIN()
        main_game.game_over()
        expected_output = "Game Over\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
