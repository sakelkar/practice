from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def mergeTwoSortedLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1, curr = l1.next, l1
            else:
                curr.next = l2
                l2, curr = l2.next, l2

        if l1 or l2:
            curr.next = l1 if not l1 else l2

        return(dummy.next)

    def mergeTwoSortedLists3(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None or l2 == None:
            return l1 or l2

        if l1.val <= l2.val:
            l1.next = self.mergeTwoSortedLists3(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoSortedLists3(l2.next, l2)
            return l2
