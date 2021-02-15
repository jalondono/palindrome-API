import unittest

from app.palindrome.utils import longest_palindromic


class TestGetPalindrome(unittest.TestCase):
    def test_get_setup(self):
        # Test to get a palindrome given one string
        self.assertEqual("abba", longest_palindromic("abba"))


class TestSpacePalindrome(unittest.TestCase):
    def test_get_setup(self):
        # Test to get a palindrome given one string with spaces
        self.assertEqual("5789875", longest_palindromic("abba 5789875"))


class TestAlphanumericPalindrome(unittest.TestCase):
    def test_get_setup(self):
        # Test to get a palindrome given an Alphanumeric String
        self.assertEqual("M*5789875*M", longest_palindromic("tr///M*5789875*M56cc//"))
