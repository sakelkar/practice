//https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
//Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
class ListNode {
	int val;
	ListNode *next;
	ListNode(): val(0), next(nullptr) {}
	ListNode(int x): val(x), next(nullptr) {}
	ListNode(int x, ListNode *next): val(x), next(next) {}
};

class Solution {
public:
	ListNode *removeDuplicatesII(ListNode *head) {
		if (!head) {
			return head;
		}

		ListNode dummy = ListNode(0);
		ListNost *prev = dummy;
		ListNode *curr = head;
		//prev pointer is used to skip duplicates nodes
		//curr pointer is basically a traversal pointer
		while (curr && curr->next) {
			if (curr->val == curr->next->val) {
				while ((curr->next) && (curr->val && curr->next->val)) {
					curr = curr->next;
				}
				//make the jump and use prev pointer for that
				prev->next = curr->next;
			} else {
				prev = prev->next;
			}
			curr = curr->next;
		} 
		return(dummy->next);
	}
};
