#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (40.89%)
# Likes:    13493
# Dislikes: 3881
# Total Accepted:    2.3M
# Total Submissions: 5.7M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
#
#
#

# @lc code=start

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # the python way
        ans = ''
        for v in zip(*strs):
            x = v[0]
            for i in v:
                if x != i:
                    return ans
            ans += x
        return ans

# @lc code=end
