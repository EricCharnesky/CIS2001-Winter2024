from unittest import TestCase
from Captain import Captain
from Calvary import Calvary

class TestCaptain(TestCase):
    def test_attack(self):
        # arrange
        expected_hit_points_before_captain = 5
        expected_hit_points = Calvary.HIT_POINTS
        us = Calvary(0,0, Calvary.TEAM_US)
        them = Calvary(0, 0, Calvary.TEAM_THEM)
        captain = Captain(0,0, Captain.TEAM_US)
        them.attack(us)

        # act
        actual_hit_points_before_captain = us.get_hit_points()
        captain.attack(us)
        actual_hit_points = us.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points_before_captain, actual_hit_points_before_captain)
        self.assertEqual(expected_hit_points, actual_hit_points)


    # more tests with same team and is alive