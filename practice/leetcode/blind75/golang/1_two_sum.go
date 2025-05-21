func twoSum(nums []int, target int) []int {
	m = make(map[int]int, 0)
	for index, num := range nums {
		complement = target - num
		if j, ok := m[complement]; ok && j != i {
			return []int{i, j}
		}
		m[num] = index
	}
	return []int{}
}
