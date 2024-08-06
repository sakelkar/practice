//https://leetcode.com/problems/longest-consecutive-sequence/description/
//Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
//You must write an algorithm that runs in O(n) time.
using namespace std;
#include <unordered_set>

class Solution {
public:
	int longestConsecutive(vector<int> &nums) {
		int best = 0;
		int start = 0;
		unordered_set<int> set;
		
		//converting to unordered set make the list only having unique elements
		//but its not ordered.
		for (int num: nums) {
			set.insert(num);
		}
		
		for (int num: nums) {
			//find the element such that its previous is not present in the set
			if (set.find(num - 1) == set.end()) {
				start = num;
				//now move forward 
				while ( set.find(start + 1) != set.end()) {
					start++;
				}
				best = max(best, start - num);
			}
 		}
		return(best);
 	}
};
