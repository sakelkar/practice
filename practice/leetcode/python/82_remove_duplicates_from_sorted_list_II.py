#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicatesII(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None

        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            if curr.val == curr.next.val:
                while ((curr.next) and (curr.val and curr.next.val)):
                    curr = curr.next
                prev.next = curr.next;
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next
