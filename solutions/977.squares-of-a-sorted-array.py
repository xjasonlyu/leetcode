#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (71.89%)
# Likes:    8325
# Dislikes: 204
# Total Accepted:    1.5M
# Total Submissions: 2.1M
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
#
#
# Example 1:
#
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
#
# Example 2:
#
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
#
#
#
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?
#

# @lc code=start

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # solution 1:
        # return sorted((n*n for n in nums))

        # solution 2:
        i = 0
        k = j = len(nums) - 1

        res = [None for _ in nums]

        while i <= j:
            x = nums[i]
            y = nums[j]

            if abs(x) > abs(y):
                res[k] = x*x
                i += 1
            else:
                res[k] = y*y
                j -= 1
            k -= 1

        return res


# @lc code=end
