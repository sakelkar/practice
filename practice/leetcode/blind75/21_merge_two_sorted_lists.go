func mergeTwoSortedLists(self, list1 *ListNode, list2 *ListNode) {
	curr = &ListNode{}
	dummy = curr

	while list1 != nil && list2 != nil {
		if list1.val < list2.val {
			curr.next = list1
			curr = list1
			list1 = list1.next
		} else {
			curr.next = list2
			curr = list2
			list2 = list2.next
		}
	}
	if list1 != nil {
		curr.next = list1
	} else {
		curr.next = list2
	}
	return dummy.next
}
