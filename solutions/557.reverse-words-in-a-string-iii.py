#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (81.91%)
# Likes:    5153
# Dislikes: 232
# Total Accepted:    725.5K
# Total Submissions: 884.8K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.
#
#
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.
#
#
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:

        return ' '.join(i[::-1] for i in s.split())

# @lc code=end
