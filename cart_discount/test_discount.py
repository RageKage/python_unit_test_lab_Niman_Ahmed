import unittest
from unittest import TestCase
from price_discount import discount, NotNumberError


class TestDiscount(TestCase):
    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_less_than_three_items(self):
        self.assertEqual(None, discount([10, 4]))

    def test_three_items_with_one_price(self):
        self.assertEqual(10, discount([10, 10, 10]))

    def test_that_list_isnt_empty(self):
        self.assertFalse(None, discount([]))

    def test_list_of_one_item(self):
        self.assertEqual(None, discount([2]))

    def test_list_of_three_items_with_float_numbers(self):
        self.assertEqual(0.3, discount([0.3, 2.3, 5]))

    def test_list_is_positive(self):
        with self.assertRaises(ValueError):
            discount([-1, 2, 3])

    def test_accept_only_numbers(self):
        with self.assertRaises(NotNumberError):
            discount(["a", 2, 3])

    # TODO more unit tests here. Each test should test one scenario


if __name__ == "__main__":
    unittest.main()
