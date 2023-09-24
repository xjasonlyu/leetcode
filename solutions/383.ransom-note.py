#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (58.33%)
# Likes:    4532
# Dislikes: 459
# Total Accepted:    898.7K
# Total Submissions: 1.5M
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
#
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
#
#
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # # Hash table solution:

        # from collections import defaultdict

        # m = defaultdict(int)

        # for i in magazine:
        #     m[i] += 1

        # for i in ransomNote:
        #     v = m.get(i, 0)
        #     if v <= 0:
        #         return False
        #     m[i] -= 1

        # return True

        # Array sln:

        a = [0] * 26

        for i in magazine:
            a[ord(i)-ord('a')] += 1

        for i in ransomNote:
            v = a[ord(i)-ord('a')]
            if v <= 0:
                return False
            a[ord(i)-ord('a')] -= 1

        return True

# @lc code=end
