class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        li = 0
        answer = 0
        for ri, char in enumerate(s):
            if char in map:
                li = max(li, map[char] + 1)
            map[char] = ri
            answer = max(answer, ri - li + 1)
        return answer

    def lengthOfLongestSubstring2(self, s: str) -> int:
        map = {}
        li = 0
        answer = 0
        for ri, char in enumerate(s):
            if char in map:
                li = max(li, map[char] + 1)
            map[char] = ri
            answer = max(answer, ri - li + 1)
        return answer

    def lengthOfLongestSubstring3(self, s: str) -> int:
        answer = 0
        li = 0
        map = {}

        for ri, char in enumerate(s):
            if char in map:
                li = max(li, map[char] + 1)
            map[char] = ri
            answer = max(answer, ri - li + 1)

        return answer

    #sliding window for length of longest substring
    #use two pointers left and right
    #left pointer is used until duplicate is not removed
    #right pointer is used to insert new character everytime
    def lengthOfLongestSubstring4(self, s: str)-> int:
        max_len = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return(max_len)

    def lengthOfLongestSubstring6(self, s: str) -> int:
        map = {}
        li = 0
        answer = 0

        for ri, char in enumerate(s):
            if char in map and map[char] >= li:
                li = map[char] + 1
            map[char] = ri
            answer = max(answer, ri - li + 1)
        return answer

    def lengthOfLongestSubstring7(self, s: str) -> int:
        seen = set()
        left = 0
        answer = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            answer = max(answer, right - left + 1)
        return answer
