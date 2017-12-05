"""
Unit tests for the superheroes API
Basic testing only
"""
import unittest
import server

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get_all_superheroes(self):
        data = server.read_superheroes()
        self.assertTrue(data)

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()