//#https://leetcode.com/problems/top-k-frequent-elements/description/
//Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

//Example 1:

//Input: nums = [1,1,1,2,2,3], k = 2
//Output: [1,2]

//Example 2:

//Input: nums = [1], k = 1
//Output: [1]

// 

//Constraints:

//    1 <= nums.length <= 105
//    -104 <= nums[i] <= 104
//    k is in the range [1, the number of unique elements in the array].
//    It is guaranteed that the answer is unique.

// 
//Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
	vector<int> topKFrequent(vector<int> &nums, int k) {
		//make the basic frequency map
		unordered_map<int, int> map;
		for (auto num: nums) {
			map[num]++;
		}
		//convert the map in the form of heap with freq as the sorting element
		priority_queue<pair<int, int>>max_heap; 
		for (auto ele: map) {
			max_heap.push(make_pair(ele.second, ele.first));
		}
		//traverse the heap for top k elements and convert the output in vector
		vector<int> result;
		for (int i = 0; i < k; i++) {
			result.push_back(max_heap.top().second);
			max_heap.pop();
		}
		return(result);
	}
};

