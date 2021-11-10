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
    return num
    # split = [int(x) for x in str(x)]
    # print(split)
    # rev = split.reverse()
    # print(rev)
    # str1 = ''.join(str(i) for i in split)
    # print(str1)
    # if x < 0:
    #     return False
    # elif x == str1:
    #     return True
    # else:
    #     return False

print(isPalindrome1(-123))
