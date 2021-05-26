import unittest

from mc_api.components.Coordinates import WrongCaretNotation
from mc_api.components.BlockCoordinates import BlockCoordinates

class TestCoordinates(unittest.TestCase):

    def test_blockcoords_zeros(self):
        coords = BlockCoordinates(0, 0, 0)

        diff = repr(coords)
        test = "0 0 0"
        self.assertEqual(diff, test)
    
    def test_coords_tilde(self):
        coords = BlockCoordinates('~', '~', '~')

        diff = repr(coords)
        test = "~ ~ ~"
        self.assertEqual(diff, test)

    def test_coords_tilde_mixed(self):
        coords = BlockCoordinates('~5', 0, '~-10')

        diff = repr(coords)
        test = "~5 0 ~-10"
        self.assertEqual(diff, test)

    def test_coords_caret(self):
        coords = BlockCoordinates('^', '^', '^')

        diff = repr(coords)
        test = "^ ^ ^"
        self.assertEqual(diff, test)

    def test_coords_caret_mixed(self):
        coords = BlockCoordinates('^5', '^-10', '^')

        diff = repr(coords)
        test = "^5 ^-10 ^"
        self.assertEqual(diff, test)

    def test_coords_caret_wrong(self):
        coords = BlockCoordinates(5, '^', '^')

        with self.assertRaises(WrongCaretNotation): 
            repr(coords)

    def test_coords_floats(self):
        coords = BlockCoordinates(1.5, '~0.1', 1)

        diff = repr(coords)
        test = "1 ~0 1"
        self.assertEqual(diff, test)

if __name__ == '__main__':
    unittest.main()
    