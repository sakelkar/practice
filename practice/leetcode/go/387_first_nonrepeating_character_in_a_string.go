//https://leetcode.com/problems/first-unique-character-in-a-string/solutions/
//Given a string s, find the first non-repeating character in it and return its index.
//If it does not exist, return -1

func firstUniqChar(s string) int {
	d := make(map(char)int)
	for i = 0; i < len(s); i++ {
		d[s[i]]++
	}
	for i = 0; i < len(s); i++ {
		if d[s[i]] == 1 {
			return i
		}
	}
	return -1
}

func firstUniqChar (s string) int {
	// allocate constant space list
	var counts = make([]int, 26)

	for i = 0; i < len(s); i++ {
		counts[s[i] - 'a']++
	}
	for i = 0; i < len(s); i++ {
		if counts[s[i] - 'a'] == 1 {
			return i
		}
	}
	return -1
}

func firstUniqChar(s string) int {
	mapChar := make(map[rune)int)

	for _, ch := range(s) {
		mapChar[ch]++
	}

	for index, ch := range(s) {
		if mapChar[ch] == 1 {
			return index
		}
	}
	return -1
}

