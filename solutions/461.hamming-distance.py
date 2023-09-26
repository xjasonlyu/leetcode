#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (75.01%)
# Likes:    3706
# Dislikes: 213
# Total Accepted:    542.1K
# Total Submissions: 721.4K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
#
# Given two integers x and y, return the Hamming distance between them.
#
#
# Example 1:
#
#
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# The above arrows point to positions where the corresponding bits are
# different.
#
#
# Example 2:
#
#
# Input: x = 3, y = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 0 <= x, y <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        r = 0

        while x or y:

            x, a = divmod(x, 2)
            y, b = divmod(y, 2)

            if a != b:
                r += 1

        return r

# @lc code=end
