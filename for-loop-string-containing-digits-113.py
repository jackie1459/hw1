"""
Exercise: Strings Containing Digits (id=113)

Write a Python function strings_containing_digits(lst) that takes a list of strings as input and returns a new list containing only the strings that contain at least one digit. 
- If no strings containing digits were found, return the string "No strings containing digits were found in the list" message.
- If the input is not a list, return "Invalid input provided" message.
- If the input list is empty, return "Empty list provided as input" message.

* Tests for the function are included. Run this script to test your function.
* To just try your function witout running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Instructions:
Your task is to implement the strings_containing_digits function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid and invalid lists.

Examples:

Valid Input:

Input: strings_containing_digits(['apple', 'banana', 'cherry', 'orange', 'pear', '123', '3 pineapples'])
Expected Output: ['123', '3 pineapples']
Explanation: The strings containing digits in the list ['apple', 'banana', 'cherry', 'orange', 'pear', '123', '3 pineapples'] are '123' and '3 pineapples'.

Invalid Input:

Input: strings_containing_digits(['apple', 'banana', 'cherry', 'orange', 'pear'])
Expected Output: "No strings containing digits were found in the list
Explanation: There are no strings containing digits in the list ['apple', 'banana', 'cherry', 'orange', 'pear'].

Input: strings_containing_digits([])
Expected Output: Empty list provided as input
Explanation: The input list is empty.

Generic Error Input:

Input: strings_containing_digits(123)
Expected Output: Invalid input provided
Explanation: The input is not a list.

"""

#def strings_containing_digits(lst):
    # <ADD YOUR CODE HERE>
  #need to handle an invalid input - use the isinstance() function to check if the input is of type list

def strings_containing_digits(lst):
    # Check if the input is a list
    if not isinstance(lst, list):
        return "Invalid input provided"

# This checks if the list is empty  
    if not lst:
        return "Empty list provided as input"


    #need to make sure there is a digit - function : 
    #We can iterate over the list and check each string using the any() function in combination with isdigit(). 
    # The isdigit() function returns True if a string contains only digits, but we need to find if any character in the string is a digit.

result = [s for s in lst if any(c.isdigit() for c in s)]

if result:
    return result
else:
        return "No strings containing digits were found in the list"

    

    pass

#=======================================
#============UNIT TESTS START===========
#=======================================
# DO NOT MODIFY THE CODE BELOW THIS LINE
import unittest

class TestStringsContainingDigits(unittest.TestCase):
            
            def test_valid_input(self):
                self.assertEqual(strings_containing_digits(['apple', 'banana', 'cherry', 'orange', 'pear', '123', '3 pineapples']), ['123', '3 pineapples'])
            
            def test_invalid_input(self):
                self.assertEqual(strings_containing_digits(['apple', 'banana', 'cherry', 'orange', 'pear']), "No strings containing digits were found in the list")
            
            def test_generic_error_input(self):
                self.assertEqual(strings_containing_digits(123), "Invalid input provided")
                
#=======================================
#===========UNIT TESTS END==============
#=======================================

if __name__ == "__main__":
    unittest.main() # This runs our unit tests. you can comment this out if you don't want to run the tests. and uncomment the following lines to just try your function.
    
    #print(strings_containing_digits(['apple', 'banana', 'cherry', 'orange', 'pear', '123', '3 pineapples']))
    #print(strings_containing_digits(['apple', 'banana', 'cherry', 'orange', 'pear']))
    