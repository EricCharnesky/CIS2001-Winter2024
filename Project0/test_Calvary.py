from unittest import TestCase
from Calvary import Calvary

class TestCalvary(TestCase):

    def test_init(self):
        expected_max_move_units = 1
        expected_attack_power = 10
        expected_hit_points = 1
        expected_range = 5
        expected_x_position = 1
        expected_y_position = 1
        expected_team = Calvary.TEAM_US

        calvary = Calvary(expected_x_position, expected_y_position , expected_team)
        actual_max_move_units = calvary._max_move_units
        actual_attack_power = calvary.get_attack_power()
        actual_hit_points = calvary.get_hit_points()
        actual_range = calvary.get_range()

        #....

        self.assertEqual(expected_range, actual_range)
        #....

