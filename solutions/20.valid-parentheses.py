#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.48%)
# Likes:    22116
# Dislikes: 1482
# Total Accepted:    3.8M
# Total Submissions: 9.4M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        x = []

        for i in s:
            if i == '(':
                x.append(i)
            elif i == '[':
                x.append(i)
            elif i == '{':
                x.append(i)
            elif i == ')' and (not len(x) or x.pop() != '('):
                return False
            elif i == ']' and (not len(x) or x.pop() != '['):
                return False
            elif i == '}' and (not len(x) or x.pop() != '{'):
                return False

        return False if len(x) else True

# @lc code=end
