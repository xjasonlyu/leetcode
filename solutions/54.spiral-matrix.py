#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (45.09%)
# Likes:    13485
# Dislikes: 1170
# Total Accepted:    1.2M
# Total Submissions: 2.5M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
#

# @lc code=start

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix[0])
        n = len(matrix)

        o = 0

        res = []

        while m > 0 and n > 0:

            for i in self.walk(matrix, m, n, o):
                res.append(i)

            m -= 2
            n -= 2
            o += 1

        return res

    @staticmethod
    def walk(a, m, n, o):

        x = y = 0

        d = 0

        loops = m*2+(n-2)*2 if m > 2 and n > 2 else m*n

        for _ in range(loops):
            yield a[x+o][y+o]

            if d == 0:
                if y < m - 1:
                    y += 1
                else:
                    d += 1
                    x += 1
            elif d == 1:
                if x < n - 1:
                    x += 1
                else:
                    d += 1
                    y -= 1
            elif d == 2:
                if y > 0:
                    y -= 1
                else:
                    d += 1
                    x -= 1
            elif d == 3:
                x -= 1

# @lc code=end
