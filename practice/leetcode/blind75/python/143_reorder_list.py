#You are given the head of a singly linked-list. The list can be represented as:
#L0 → L1 → … → Ln - 1 → Ln
#Reorder the list to be on the following form:
#L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

#L0 -> L1 -> L2 -> Ln/2
#Ln -> Ln-1 -> Ln-2 -> Ln/2-1

#You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
#Example 1:
#Input: head = [1,2,3,4]
#Output: [1,4,2,3]
#
#Example 2:
#Input: head = [1,2,3,4,5]
#Output: [1,5,2,4,3]
#
#Constraints:
#    The number of nodes in the list is in the range [1, 5 * 104].
#    1 <= Node.val <= 1000
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def reverseList(head):
            prev, curr = None, head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        #split the list in two halves
        #keep the first half as it is
        #rever the 2nd half
        #have slow and 2 times fast than slow pointer
        slow, fast = head, head.next
        while fast and fast.next:
            if slow:
                slow = slow.next

            if fast and fast.next:
                fast = fast.next.next

        #now slow.next is the head of the 2nd half
        if slow:
            h2 = reverseList(slow.next)

        #now h2 is pointing to reversed to 2nd half so its something like
        #Ln -> Ln-1 -> Ln-2...Ln/2 - 1

        #how to interleave the two lists one slow list
        #and 2nd list which is reversed 2nd half
        dummyNode = ListNode(-1)
        h1, curr = head, dummyNode
        #dummynode is pointing to previous node of the head
        index = 0

        #use index to to interleave, when index%2 = 1 use h1 and when its zero use h2
        while h1 or h2:
            if h1 and curr and index % 2 == 0:
                curr.next, h1 = h1, h1.next
            elif h2 and curr:
                curr.next, h2 = h2, h2.next
            index += 1
            if curr:
                curr = curr.next

        return dummyNode.next


