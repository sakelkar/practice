#https://leetcode.com/problems/merge-k-sorted-lists/
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.
from typing import Optional
from typing import List
from heapq import heappush
from heapq import heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKSortedLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoSortedLists(l1, l2):
            tail = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1, tail = l1.next, l1
                else:
                    tail.next = l2
                    l2, tail = l2.next, l2

            if l1:
                tail.next = l1
            else:
                tail.next = l2

            return(dummy.next)

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergeLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergeLists.append(mergeTwoSortedLists(l1, l2))

            lists = mergeLists
        return lists[0]

#priority queue implementation
class Solution2:
    def mergeKSortedLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        h = []
        for i, l in enumerate(lists):
            if l: heappush(h, (l.val, i))

        tail = dummy = ListNode(0)

        while h:
            val, i = heappop(h)
            tail.next = ListNode(val)
            if lists[i].next:
                heappush(h, (lists[i].next.val, i))
                lists[i] = lists[i].next
            tail = tail.next
        return(dummy.next)
        
