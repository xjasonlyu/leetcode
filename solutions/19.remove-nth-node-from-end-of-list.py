#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (41.18%)
# Likes:    17192
# Dislikes: 706
# Total Accepted:    2.2M
# Total Submissions: 5.2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
# Example 2:
#
#
# Input: head = [1], n = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
#
# Follow up: Could you do this in one pass?
#
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(-1, next=head)

        f = s = d

        # c = 0
        # while f:

        #     if c <= n:
        #         c += 1
        #     else:
        #         s = s.next

        #     f = f.next

        for _ in range(n+1):
            f = f.next

        while f:
            s = s.next
            f = f.next

        s.next = s.next.next

        return d.next


# @lc code=end
