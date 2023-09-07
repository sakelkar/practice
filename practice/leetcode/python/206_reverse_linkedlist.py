#https://leetcode.com/problems/reverse-linked-list/
#Given the head of a singly linked list, reverse the list, and return the reversed list.

#Definition of singly linked list
#class ListNode:
#   def __init__(self, val=0, next=None)
#       self.val = val
#       self.next = next
#typing module is create to support gradual typing as per PEP 484

from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while (curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return(curr)

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None
        return(newHead)
