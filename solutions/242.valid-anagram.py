#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.08%)
# Likes:    10622
# Dislikes: 331
# Total Accepted:    2.6M
# Total Submissions: 4.2M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # sort lists:

        # return sorted(s) == sorted(t)

        m = {}

        for i in s:
            m.setdefault(i, 0)
            m[i] += 1

        for i in t:
            m.setdefault(i, 0)
            m[i] -= 1

        for i in m.values():
            if i != 0:
                return False

        return True

# @lc code=end
