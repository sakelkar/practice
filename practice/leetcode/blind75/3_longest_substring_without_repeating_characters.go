func lengthOfLongestSubstring(s string) int {
	m := make(map[rune]int, 0)
	li := 0
	answer := 0

	for ri, char := range []rune(s) {
		if prevIndex, found := m[char]; found && prevIndex >= li {
			li = prevIndex + 1
		}
		m[char] = ri
		if currentLength := ri - li + 1; currentLength > answer {
			answer = currentLength
		}
	}
}
