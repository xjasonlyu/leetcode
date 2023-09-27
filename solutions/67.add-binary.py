#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (52.40%)
# Likes:    8757
# Dislikes: 870
# Total Accepted:    1.3M
# Total Submissions: 2.4M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
#
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
#
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
#
#
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # # PY WAY:
        # return bin(int(a, 2)+int(b, 2))[2:]

        r = ''
        c = 0

        i = -1

        while True:
            x = int(a[i])if -i-1 < len(a) else 0
            y = int(b[i]) if -i-1 < len(b) else 0

            n = x + y + c

            if -i > max(len(a), len(b)) and not c:
                break

            c, n = divmod(n, 2)

            r = str(n) + r

            i -= 1

        return r

# @lc code=end
