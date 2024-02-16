#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (45.45%)
# Likes:    10815
# Dislikes: 497
# Total Accepted:    751.9K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
#
# Example 2:
#
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
#
# Follow up: Could you do it in one pass?
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # stack solution: O(n) / O(n)
        
        dummy = ListNode(next=head)

        s = []

        i = 0
        h = dummy
        while h:

            if left <= i <= right:
                s.append(h.val)

            i += 1
            h = h.next

        i = 0
        h = dummy
        while h:

            if left <= i and s:
                h.val = s.pop()

            i += 1
            h = h.next

        return dummy.next


# @lc code=end
