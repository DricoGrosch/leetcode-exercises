from unittest import TestCase
from src.easy.palindrome_string import Solution as PalindromeSolution
class TestEasyExercises(TestCase):


    def test_is_palindrome(self):
        solution = PalindromeSolution()
        self.assertTrue(solution.isPalindrome("A man, a plan, a canal: Panama"))