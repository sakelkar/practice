#https://leetcode.com/problems/swap-nodes-in-pairs/
#Given a linked list, swap every two adjacent nodes and return its head.
#You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            nextPair = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = nextPair
            prev.next = second

            prev = curr
            curr = nextPair
        return(dummy.next)
