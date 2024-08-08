#https://leetcode.com/problems/rotate-list/description/
#Given the head of a linked list, rotate the list to the right by k places.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], K: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        N = 1
        while curr.next:
            N += 1
            curr = curr.next

        curr.next = head
        K = K % N

        if K:
            for _ in range(N - K - 1):
                if curr: 
                    curr = curr.next

        if curr: 
            head = curr.next
            curr.next = None
            return(head)
