# Implementation of the largest_number function
def largest_number(numbers):
    # Base case: 
    if len(numbers) == 1:
        return numbers[0]
    else:
        # Recursive case: 
        max_rest = largest_number(numbers[1:])
        # Return the larger of the two
        return numbers[0] if numbers[0] > max_rest else max_rest

# Unit tests for the largest_number function
import unittest

class TestLargestNumber(unittest.TestCase):
    def test_general_case(self):
        numbers = [10, 5, 25, 8, 17]
        self.assertEqual(largest_number(numbers), 25)

    def test_single_element(self):
        numbers = [100]
        self.assertEqual(largest_number(numbers), 100)

    def test_negative_numbers(self):
        numbers = [-10, -5, -25, -8, -17]
        self.assertEqual(largest_number(numbers), -5)

if __name__ == '__main__':
    unittest.main()