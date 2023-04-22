#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (53.59%)
# Likes:    9317
# Dislikes: 2482
# Total Accepted:    3.1M
# Total Submissions: 5.8M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
#
# Example 1:
#
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
#
# Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without converting the integer to a string?
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # the python way
        # return str(x) == str(x)[::-1]

        # Convert to string
        #
        # s = str(x)
        # i = 0
        # j = len(s) - 1
        # while i <= j:
        #     if s[i] != s[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True

        # Math operation
        if x < 0:
            return False
        i = x
        y = 0
        while i > 0:
            y = y*10+i % 10
            i //= 10
        return x == y

# @lc code=end
