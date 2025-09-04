#Given the head of a singly linked list, reverse the list, and return the reversed list.
#Example 1:
#
#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]
#
#Example 2:
#
#Input: head = [1,2]
#Output: [2,1]
#
#Example 3:
#
#Input: head = []
#Output: []
#
#Constraints:
#
#    The number of nodes in the list is the range [0, 5000].
#    -5000 <= Node.val <= 5000
#Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #flow of the logic is as follows
        prev, curr = None, head

        #capture the next node reference in temp variable
        #make current.next poitn to previous to make reversion possible
        #move previous to curr
        #move curr to next which is stored in step 1
        #do all of this till the curr is valid.
        #when you reach end curr would have become None and you would exit the loop
        while (curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

