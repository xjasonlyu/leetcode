#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Medium (27.47%)
# Likes:    11809
# Dislikes: 12924
# Total Accepted:    2.8M
# Total Submissions: 10.1M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
#
#
# Example 1:
#
#
# Input: x = 123
# Output: 321
#
#
# Example 2:
#
#
# Input: x = -123
# Output: -321
#
#
# Example 3:
#
#
# Input: x = 120
# Output: 21
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:

        # # Py way:

        # r = (x//abs(x) if x else 1)*int(str(abs(x))[::-1])

        # return r if -2**31 <= r <= 2**31 - 1 else 0

        # human way:

        r = 0
        s = 1 if x >= 0 else -1
        x = abs(x)

        while x:

            x, m = divmod(x, 10)

            r = r*10+m

        return s*r if -2**31 <= s*r <= 2**31 - 1 else 0

# @lc code=end
