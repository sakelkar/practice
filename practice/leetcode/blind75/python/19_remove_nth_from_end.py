from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode()
        dummy.next = head
        ahead = head
        behind = dummy

        while n > 0 and ahead:
            ahead = ahead.next
            n -= 1

        while ahead:
            ahead = ahead.next
            behind = behind.next

        #remove the target node
        if behind.next:
            behind.next = behind.next.next

        return dummy.next
