"""
Exercise: Character Occurrence Count Challenge (id=122)
* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python function count_occurrences(string, char) that takes a string string and a character char as 
arguments and returns the number of occurrences of the character in the string using a while loop.
Your function should adhere to the following requirements:

The function should take two arguments: a string string and a character char.
The function should return the number of occurrences of the character char in the string.
If the input value for string is not a string or if the input value for char is not a single character, your program should return the message "Invalid input provided."
Tests for the function are included. Run this script to test your function.
To just try your function without running the tests, uncomment your function from the if __name__ == '__main__': block.

Instructions:

Your task is to implement the program according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid and invalid inputs.

Example:

Valid Input:

Input: "Hello, World!", "o"
Expected Output: 2
Explanation: The character 'o' occurs twice in the string "Hello, World!".

Invalid Input:

Input: 12345, "2"
Expected Output: Invalid input provided
Explanation: The input value for string is not a string.

Invalid Input:

Input: "Hello, World!", "oo"
Expected Output: Invalid input provided
Explanation: The input value for char is not a single character.


"""
def count_occurrences(string, char):
    # <ADD YOUR CODE HERE>
    pass


#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest


class TestCharacterOccurrenceCount(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(count_occurrences("Hello, World!", "o"), 2)

    def test_invalid_input_string(self):
        self.assertEqual(count_occurrences(12345, "2"), "Invalid input provided")

    def test_invalid_input_char(self):
        self.assertEqual(count_occurrences("Hello, World!", "oo"), "Invalid input provided")


if __name__ == "__main__":
    unittest.main()