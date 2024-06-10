## Overview
This project contains a Python function to find the largest number in a list using recursion, as well as a set of unit tests to verify its correctness.



**Function:**   largest_number


***Description***

The largest_number function takes a list of integers as input and returns the largest integer in the list. It uses a recursive approach to solve the problem.


***Implementation***
The function works as follows:


**Base Case:** If the list contains only one element, return that element.
**Recursive Case:** Compare the first element of the list with the largest number in the rest of the list (found by a recursive call) and return the larger of the two.




### Unit Tests


**Description**

The unit tests verify the correctness of the largest_number function. They cover general cases, single-element lists, and lists with negative numbers.


***Implementation***

The tests are implemented using Python's built-in unittest framework.


***Running the Tests***

To run the tests, execute the following command in your terminal:
python -m unittest <name_of_the_test_file>.py
Replace <name_of_the_test_file> with the name of your Python file containing the unit tests.


***Conclusion***

This project demonstrates a simple recursive function to find the largest number in a list and a corresponding set of unit tests to ensure its functionality. The use of recursion and unit testing showcases fundamental programming concepts in Python.
