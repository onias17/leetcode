'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1
'''

# SOLUTION 1
def isPalindrome(num):
    return str(num) == str(num)[::-1]

print(isPalindrome(-123))

# SOLUTION 2
def isPalindrome1(num):
    str1 = str(num)
    print(str1)
    str2 = str1[::-1]
    print(str2)
    if str1 == str2:
        return True
    else:
        return False

print(isPalindrome1(202))
