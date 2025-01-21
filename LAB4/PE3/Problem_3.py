import unittest
import oxo_dialog_ui

class TestDialogUI(unittest.TestCase):
    def setUp(self):
        self.empty_board = [" "] * 9

    def test_startGame_returns_empty_board(self):
        result = oxo_dialog_ui.startGame()
        self.assertEqual(result, self.empty_board,)

    def test_startGame_board_length(self):
        result = oxo_dialog_ui.startGame()
        self.assertEqual(len(result), 9,)

    def test_startGame_board_is_list(self):
        result = oxo_dialog_ui.startGame()
        self.assertIsInstance(result, list,)

if __name__ == "__main__":
    unittest.main()
