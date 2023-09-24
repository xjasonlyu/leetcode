#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (57.19%)
# Likes:    4755
# Dislikes: 135
# Total Accepted:    306.2K
# Total Submissions: 536K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
# return the number of tuples (i, j, k, l) such that:
#
#
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#
#
#
# Example 1:
#
#
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) +
# (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) +
# (-1) + 0 = 0
#
#
# Example 2:
#
#
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
#
#
#
# Constraints:
#
#
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
#
#
#

# @lc code=start

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        # # Brute solution: (time exceeded)
        #
        # c = 0
        # for ki, vi in enumerate(nums1):
        #     for kj, vj in enumerate(nums2):
        #         for km, vm in enumerate(nums3):
        #             for kn, vn in enumerate(nums4):
        #                 if vi + vj + vm + vn == 0:
        #                     c += 1
        # return c

        from collections import defaultdict

        c = 0

        ma = defaultdict(int)
        # mb = defaultdict(int)

        for i in nums1:
            for j in nums2:
                ma[i + j] += 1

        for i in nums3:
            for j in nums4:
                if -(i+j) in ma:
                    c += ma[-(i+j)]

        return c


# @lc code=end
