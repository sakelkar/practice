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
