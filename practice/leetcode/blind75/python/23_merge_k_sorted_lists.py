from typing import Optional

class Solution:
    def mergeKSortedLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoSortedLists(l1, l2):
            curr = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    curr = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    curr = l2
                    l2 = l2.next

            if l1:
                curr.next = l1
            else:
                curr.next = l2
            return dummy.next

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(mergeTwoSortedLists(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeKSortedLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwoSortedLists(l1, l2):
            curr = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1, curr = l1.next, l1
                else:
                    curr.next = l2
                    l2, curr = l2.next, l2
            curr.next = l1 if l1 else l2
            return dummy.next

        if not lists or len(lists):
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergeLists.append(mergeTwoSortedLists(l1, l2))
            lists = mergedLists
        return(lists[0])
