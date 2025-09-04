#Given head, the head of a linked list, determine if the linked list has a cycle in it.
#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#Return true if there is a cycle in the linked list. Otherwise, return false.
#
#Example 1:
#Input: head = [3,2,0,-4], pos = 1
#Output: true
#Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#
#Example 2:
#Input: head = [1,2], pos = 0
#Output: true
#Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

#Example 3:
#Input: head = [1], pos = -1
#Output: false
#Explanation: There is no cycle in the linked list.
#
#Constraints:
#    The number of the nodes in the list is in the range [0, 104].
#    -105 <= Node.val <= 105
#    pos is -1 or a valid index in the linked-list.
#
#Follow up: Can you solve it using O(1) (i.e. constant) memory?
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#some basic simple but critical points
#for there to be cycle there head and head.next cannot be None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        #now while iterating fast must be jumping by 2 and slow must be jumping by 1
        #so slow will move = slow.next and fast will move fast.next.next
        #hence in a while loop fast.next and fast.next.next shuold be checked
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

