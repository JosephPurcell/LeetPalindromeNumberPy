from unittest import TestCase
from main import Solution


class TestSolution(TestCase):
    def test_is_palindrome1(self):
        solution = Solution()
        output = solution.isPalindrome(121)
        self.assertTrue(output)

    def test_is_palindrome2(self):
        solution = Solution()
        output = solution.isPalindrome(1221)
        self.assertTrue(output)

    def test_is_palindrome3(self):
        solution = Solution()
        output = solution.isPalindrome(-121)
        self.assertFalse(output)

    def test_is_palindrome4(self):
        solution = Solution()
        output = solution.isPalindrome(-121)
        self.assertFalse(output)

    def test_is_palindrome5(self):
        solution = Solution()
        output = solution.isPalindrome(9)
        self.assertTrue(output)