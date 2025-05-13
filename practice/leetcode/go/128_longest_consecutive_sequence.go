//https://leetcode.com/problems/longest-consecutive-sequence/description/
//Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
//You must write an algorithm that runs in O(n) time.
func longestConsecutiveSequence(nums []int) int {
	set := make(map[int]bool, 0)
	result := 0
	for _, num := range nums {
		set[num] = true
	}
	for num := range set {
		if set[num - 1] {
			continue
		}
		count := 1
		for i = num + 1; set[i]; i++ {
			count++
		}
		result = max(result, count)
	}
	return result
}
// longestConsecutiveSequence2
func longestConsecutiveSequence2(nums []int) int {
	set := make(map[int]bool, 0)
	result := 0

	for _, num := range nums {
		if set[num] = true
	}
	for num := range set {
		if set[num-1] {
			continue
		}
		count := 1
		for i = num + 1; set[i]; i++ {
			count++
		}
		result = max(result, count)
	}
	return(result)
}
