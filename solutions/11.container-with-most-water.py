#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (53.99%)
# Likes:    28090
# Dislikes: 1635
# Total Accepted:    2.7M
# Total Submissions: 5M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

# @lc code=start

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n^2) solution:
        # (time exceeded)
        # l = len(height)
        # res = 0
        # for i in range(l-1):
        #     for j in range(i+1, l):
        #         res = max(res, min(height[i], height[j])*abs(j-i))
        # return res

        #two pointers:
        l = 0
        r = len(height) - 1

        res = 0
        while l < r:
            res = max(res, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
        
# @lc code=end

