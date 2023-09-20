#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (67.47%)
# Likes:    6010
# Dislikes: 239
# Total Accepted:    519.1K
# Total Submissions: 740.3K
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
#
#
#

# @lc code=start

from typing import List


class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]

        i = 1
        offset = 0

        while n > 0:

            i = draw(res, n, i, offset)

            offset += 1
            n -= 2

        return res


def draw(a, n, i, offset):

    if n == 1:
        a[offset][offset] = i
        return i+1

    x = y = 0

    d = 0

    for _ in range(4*(n-1)):

        # print(x, y, i, d)

        a[offset+x][offset+y] = i

        if d % 4 == 0:
            if y < n - 1:
                y += 1
            else:
                d += 1
                x += 1
        elif d % 4 == 1:
            if x < n - 1:
                x += 1
            else:
                d += 1
                y -= 1
        elif d % 4 == 2:
            if y > 0:
                y -= 1
            else:
                d += 1
                x -= 1
        elif d % 4 == 3:
            if x > 1:
                x -= 1

        i += 1

    return i


# @lc code=end
