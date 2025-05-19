func mergeKLists(lists []*ListNode) *ListNode {
	if !lists or len(lists) == 0 {
		return nil
	}

	for len(lists) > 1 {
		l1 := lists[0]
		l1 := lists[1]
		lists := lists[2:]
		merged := mergeTwoSortedLists(l1, l2)
		lists = append(lists, merged)
	}
	return lists[0]
}

func mergeTwoSortedLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := &ListNode{}
	node := dummy

	while list1 != nil && list2 != nil {
		if list1.val < list2.val {
			node.next = list1
			node = list1
			list1 = list1.next
		} else {
			node.next = list2
			node = list2
			list2 = list2.next
		}
	}
	if list1 != nil {
		node.next = list1
	} else {
		node.next = list2
	}
	return dummy.next
}
