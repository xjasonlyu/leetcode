#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (45.03%)
# Likes:    11653
# Dislikes: 338
# Total Accepted:    847.8K
# Total Submissions: 1.8M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to
# target. If there is no such subarray, return 0 instead.
#
#
# Example 1:
#
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
#
#
# Example 2:
#
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
#
# Example 3:
#
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)).
#

# @lc code=start

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # l = len(nums)
        # res = float('inf')
        # for i in range(l):
        #     s = 0
        #     for j in range(i, l):
        #         s += nums[j]
        #         if s >= target:
        #             res = min(j-i+1, res)
        #             break
        # return res if res != float('inf') else 0

        i = j = 0
        res = float('inf')

        s = nums[0]
        while i <= j < len(nums):
            if s >= target:
                res = min(j-i+1, res)
                s -= nums[i]
                i += 1
            else:
                j += 1
                s += nums[j] if j < len(nums) else 0

        return res if res != float('inf') else 0


# @lc code=end
