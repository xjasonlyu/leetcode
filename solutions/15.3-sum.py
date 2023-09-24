#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (32.62%)
# Likes:    28435
# Dislikes: 2557
# Total Accepted:    2.9M
# Total Submissions: 8.8M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
# Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
# Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Hash table (but slow):

        m = {}

        res = []

        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

        k = sorted(m.keys())

        for idx, i in enumerate(k):

            if i > 0:
                continue

            m[i] -= 1

            for j in k[idx:]:

                if m[j] > 0:

                    m[j] -= 1

                    if m.get(-(i+j), -1) > 0 and -(i+j) >= j:
                        res.append([i, j, -(i+j)])

                    m[j] += 1

            m[i] += 1

        return res

# @lc code=end
