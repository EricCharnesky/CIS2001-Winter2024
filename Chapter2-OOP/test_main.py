from unittest import TestCase
from main import Item

class TestItem(TestCase):
    # test the gets with the init
    def test_init(self):
        # AAA convention

        # Arrange - setup the variables we need to test
        expected_name = "Apples"
        expected_unit_price = 1.1
        expected_quantity = 2
        expected_total_price = 2.2

        # Act - call the code we're testing - and get values
        apples = Item(expected_name, expected_quantity, expected_unit_price)
        actual_name = apples.get_name()
        actual_quantity = apples.get_quantity()
        actual_unit_price = apples.get_unit_price()
        actual_total_price = apples.get_total_price()

        # Assert - did we get what we expected?
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_quantity, actual_quantity)
        self.assertEqual(expected_unit_price, actual_unit_price)
        self.assertEqual(expected_total_price, actual_total_price)


    def test_set_unit_price_less_than_0(self):
        # AAA convention

        # Arrange - setup the variables we need to test
        expected_unit_price = 0
        apples = Item("", 0, 2)

        # Act - call the code we're testing - and get values
        apples.set_unit_price(-2)
        actual_unit_price = apples.get_unit_price()

        # Assert - did we get what we expected?
        self.assertEqual(expected_unit_price, actual_unit_price)

    def test_set_quantity_less_than_0(self):
        # AAA convention

        # Arrange - setup the variables we need to test
        expected_quantity = 0
        apples = Item("", 2, 0)

        # Act - call the code we're testing - and get values
        apples.set_quantity(-2)
        actual_quantity = apples.get_quantity()

        # Assert - did we get what we expected?
        self.assertEqual(expected_quantity, actual_quantity)
