from unittest import TestCase
from Unit import Unit

class TestUnit(TestCase):
    def test_attack(self):
        # arrange
        expected_hit_points = 0
        us = Unit(10, 10, 2, 0, 0, Unit.TEAM_US, 1)
        them = Unit(10, 10, 2, 1, 1, Unit.TEAM_THEM, 1)

        # act
        us.attack(them)
        actual_hit_points = them.get_hit_points()
        actual_is_alive = them.is_alive()

        # assert
        self.assertEqual(expected_hit_points, actual_hit_points)
        self.assertFalse(actual_is_alive)

    def test_attack_not_alive_doesnt_attack(self):
        # arrange
        expected_hit_points = 10
        us = Unit(10, 10, 2, 0, 0, Unit.TEAM_US, 1)
        them = Unit(10, 10, 2, 1, 1, Unit.TEAM_THEM, 1)
        us.attack(them)

        # act
        them.attack(us)
        actual_hit_points = us.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points, actual_hit_points)

    def test_attack_not_within_range(self):
        # arrange
        expected_hit_points = 10
        us = Unit(10, expected_hit_points, 1, 0, 0, Unit.TEAM_US, 1)
        them = Unit(10, expected_hit_points, 1, 1, 1, Unit.TEAM_THEM, 1)

        # act
        us.attack(them)
        actual_hit_points = them.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points, actual_hit_points)

    def test_attack_same_team(self):
        # arrange
        expected_hit_points = 10
        us = Unit(10, expected_hit_points, 2, 0, 0, Unit.TEAM_US, 1)
        them = Unit(10, expected_hit_points, 2, 1, 1, Unit.TEAM_US, 1)

        # act
        us.attack(them)
        actual_hit_points = them.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points, actual_hit_points)

    # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
    def test_move_throws(self):

        # arrange
        us = Unit(10, 10, 2, 0, 0, Unit.TEAM_US, 1)
        expected_error_message = "Can't move x and y"

        # act
        with self.assertRaises(ValueError) as error:
            us.move(10, 10)

        # assert
        self.assertTrue(expected_error_message in str(error.exception))

    def test_move(self):

        # arrange
        us = Unit(10, 10, 2, 0, 0, Unit.TEAM_US, 2)
        expected_x_position = 2

        # act
        us.move(10, 0)
        actual_x_position = us.get_x_position()

        # assert
        self.assertEqual(expected_x_position, actual_x_position)
