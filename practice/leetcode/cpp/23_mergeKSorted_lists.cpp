#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(): val(0), next(nullptr) {}
	ListNode(int x): val(x), next(nullptr) {}
    ListNode(int x, ListNode *next): val(x), next(next) {}
};

class Solution {
private:
	ListNode *mergeTwoSortedLists(ListNode *l1, ListNode *l2) {
		if (!l1 and !l2)
			return nullptr;
		if (!l1 and l2) 
			return l2;
		if (l1 and !l2) 
			return l1;

		ListNode *head = nullptr;
		ListNode *temp = nullptr;
		
		if (l1->val < l2->val) {
			head = l1;
			l1 = l1->next;
		} else {
			head = l2;
			l2 = l2->next;
		}
		temp = head;
		while (l1 and l2) {
			if (l1->val < l2->val) {
				temp->next = l1;
				l1 = l1->next;
			} else {
				temp->next = l2;
				l2 = l2->next;
			}
			temp = temp->next;
		}
		if (l1) {
			temp->next = l1;
		} else {
			temp->next = l2;
		}
		return head;
	}
public:

	ListNode *mergeKSortedLists(vector<ListNode *>&lists) {
		if (lists.empty()) {
			return nullptr;
		}
		while (lists.size() > 1) {
			lists.push_back(mergeTwoSortedLists(lists[0], lists[1]));
			lists.erase(lists.begin());
			lists.erase(lists.begin());
		}
		return(lists.front());
	} 
};

class Solution2 {
public:
	struct compare {
		bool operator()(const ListNode *l, const ListNode *r) {
			return(l->val > r->val);
		}
	};
	ListNode *mergeKSortedLists(vector<ListNode *> lists) {
		priority_queue<ListNode *, vector<ListNode *>, compare> q;
		if (lists.empty()) {
			return nullptr;
		}
		for (auto l: lists) {
			q.push(l);
		}
		ListNode *answer = q.top();
		q.pop();
		if (answer->next) {
			q.push(answer->next);
		}
		ListNode *tail = answer;
		while (!q.empty()) {
			tail->next = q.top();
			q.pop();
			tail = tail->next;
			if (tail->next) {
				q.push(tail->next);
			}
		}
		return(answer);
 	}
};
