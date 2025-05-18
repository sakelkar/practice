func longestConsecutive(nums []int) int {
	set := make(map[int]bool, 0)
	result := 0
	for _, num := range nums {
		set[num] = true
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
