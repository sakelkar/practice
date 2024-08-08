//https://leetcode.com/problems/rotate-list/description/
//Given the head of a linked list, rotate the list to the right by k places.

struct ListNode {
	int val;
	ListNode *next;
	ListNode(): val(0), next(nullptr) {}
	ListNode(int x): val(x), next(nullptr) {}
	ListNode(int x, ListNode *next): val(x), next(next) {}
};

class Solution {
public:
	ListNode *rotateRight(ListNode *head, int k) {
		//3. mark the N - K - 1 th element next = null as last element and
		//3. mark the N - Kth element as head
		int N = 1;
		ListNode *curr = head;
		if (!head) {
			return nullptr;
		}
		//1. count the number of nodes in the list say N
		while (curr->next) {
			N++;
			curr = curr->next;
		}
		//2. create the circular list for ease of traversal
		curr->next = head;
		//3. rotate by K means that the new head will be at N - kth element
		//actual effective rotation by K will be equal to k = k % N
		if (k = k % N) {
			for (int i = 0; i < N - k; i++) {
				curr = curr->next;
			}
		}
		head = curr->next;
		curr->next = nullptr;
		return(head);
		
	}
};
