##https://leetcode.com/problems/top-k-frequent-elements/description/
#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

#Example 1:

#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

#Example 2:

#Input: nums = [1], k = 1
#Output: [1]

# 

#Constraints:

#    1 <= nums.length <= 105
#    -104 <= nums[i] <= 104
#    k is in the range [1, the number of unique elements in the array].
#    It is guaranteed that the answer is unique.

# 
#Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
import collections
from typing import Collection, Counter, List
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #create a frequency map of each number
        counts = Counter[nums]

        #create a new KV store where key will be frequency and value will be list of numbers 
        freqToNumsListsMap = collections.defaultdict(list)
        for val, freq in counts.items():
            freqToNumsListsMap[freq].append(val)

        freqHeap = [-freq for freq in freqToNumsListsMap.keys()]
        heapq.heapify(freqHeap)

        answer = []

        for i in range(len(freqHeap)):
            freq = - heapq.heappop(freqHeap)
            for num in freqToNumsListsMap[freq]:
                if len(answer) == k:
                    return(answer)
                answer.append(num)
        return(answer)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        sorted_map = dict(sorted(map.items(), key=lambda x: x[1], reverse=True)[:k])
        return list(sorted_map.keys())

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        sorted_map = dict(sorted(freqMap.items(), key=lambda x:x[1], reverse=True)[:k])
        return list(sorted_map.keys())


    def topKFrequentNBucketSort(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        freq = Counter(nums)  
        # Example: nums = [1,1,1,2,2,3]
        # freq = {1: 3, 2: 2, 3: 1}
        
        # Step 2: Create buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        # Example: len(nums) = 6 → buckets = [[], [], [], [], [], [], []]
        
        # Fill buckets: place each num in its frequency index
        for num, count in freq.items():
            buckets[count].append(num)
        # buckets = [[], [3], [2], [1], [], [], []]
        # index 1 → [3] (3 appears once)
        # index 2 → [2] (2 appears twice)
        # index 3 → [1] (1 appears thrice)
        
        # Step 3: Traverse from high freq to low freq
        res = []
        for i in range(len(buckets) - 1, 0, -1):  # from n down to 1
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

    #top K frequent element using bucket sort
    def topKFreq(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return []

    def topKFancy(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_map = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True)[:k])
        return list(sorted_map.keys())


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]

    #min_heap based solution
    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]


