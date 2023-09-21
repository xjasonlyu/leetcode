#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Medium (27.67%)
# Likes:    2416
# Dislikes: 1520
# Total Accepted:    283.7K
# Total Submissions: 1M
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' +
# '[[],[1],[3],[1,2],[1],[1],[1]]'
#
# Design your implementation of the linked list. You can choose to use a singly
# or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val
# is the value of the current node, and next is a pointer/reference to the next
# node.
# If you want to use the doubly linked list, you will need one more attribute
# prev to indicate the previous node in the linked list. Assume all nodes in
# the linked list are 0-indexed.
#
# Implement the MyLinkedList class:
#
#
# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the index^th node in the linked list. If
# the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of
# the linked list. After the insertion, the new node will be the first node of
# the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the
# linked list.
# void addAtIndex(int index, int val) Add a node of value val before the
# index^th node in the linked list. If index equals the length of the linked
# list, the node will be appended to the end of the linked list. If index is
# greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the index^th node in the linked list, if
# the index is valid.
#
#
#
# Example 1:
#
#
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
#
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
#
#
#
# Constraints:
#
#
# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and
# deleteAtIndex.
#
#
#

# @lc code=start

class node:

    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: node = next


class MyLinkedList:

    def __init__(self):

        self.node = node(-1)
        self.size = 0

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:
            return -1

        h = self.node.next

        for _ in range(index):
            h = h.next

        return h.val

    def addAtHead(self, val: int) -> None:
        # self.size += 1
        # self.node.next = node(val, next=self.node.next)

        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        # h = self.node

        # for _ in range(self.size):
        #     h = h.next

        # h.next = node(val)
        # self.size += 1

        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index > self.size:
            return

        h = self.node

        for _ in range(index):
            h = h.next

        h.next = node(val, next=h.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:
            return

        h = self.node

        for _ in range(index):
            h = h.next

        h.next = h.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
