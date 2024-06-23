from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
import unittest
from src.medium.jump_game_2 import Solution as SolutionJump2 
from src.medium.jump_game import Solution as SolutionJump1

class TestMediumExercises(unittest.TestCase):
    def test_jump_game_1(self):
        solution = SolutionJump1()
        self.assertEqual(solution.canJump([3,0,8,2,0,0,1]) , True)
        self.assertEqual(solution.canJump([2,3,1,1,4]) , True)
        self.assertEqual(solution.canJump([3,2,1,0,4]) , False)
        self.assertEqual(solution.canJump([0]) , True)
        self.assertEqual(solution.canJump([2,5,0,0]) , True)

    def test_jump_game_2(self):
        solution = SolutionJump2()
        self.assertEqual(solution.jump([4,1,1,3,1,1,1]),2)
        self.assertEqual(solution.jump([1,2,1,1,1]),3)
        self.assertEqual(solution.jump([2,3,1,1,4]),2)
        self.assertEqual(solution.jump([2,3,0,1,4]),2)
        self.assertEqual(solution.jump([0]),0)
        self.assertEqual(solution.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]),2)

        