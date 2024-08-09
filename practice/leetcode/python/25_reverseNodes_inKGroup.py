#https://leetcode.com/problems/reverse-nodes-in-k-group/
#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#You may not alter the values in the list's nodes, only nodes themselves may be changed.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            #get kth node for current group to be reversed
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next
            if groupPrev:
                prev, curr = kth.next, groupPrev.next

            while curr and curr != groupNext:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return(dummy.next)

    def getKth(self, prev, k):
        while prev and k > 0:
            prev = prev.next
            k -= 1

class ListNode2:
    def __init__(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def ll_length(head):
            N = 0
            while head:
                N += 1;
                head = head.next


class Solution:
    def reverseKGroup(self, head: Option[ListNode], K: int) -> Optional[ListNode]:
        #1. find out the length of linked list say N
        #2. return if N < K
        #3. use two pointer reversal for loop for 0 to N/K times.
        def ll_length(head):
            N = 0
            while head:
                head = head.next
                N += 1
            return N

        N = ll_length(head)    
        if N < K:
            return head

        dummy = ListNode(0, head)
        prev = dummy


        for _ in range(N/K):
            for _ in range(K):
                temp = prev.next
                prev.next = head.next
                head.next = head.next.next
                prev.next.next = temp
            prev = head
            curr = head.next
        return(dummy.next)
