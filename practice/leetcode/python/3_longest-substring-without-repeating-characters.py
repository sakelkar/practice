#https://leetcode.com/problems/longest-substring-without-repeating-characters/

#Given a string s, find the length of the longest
#substring without repeating characters.

class Solution:
    def lengthOfLongestSubstrng(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return(res)

    def lengthOfLongestSubstring2(self, s: str) -> int:
        left = 0
        seen = {}
        length = 0
        for right, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char] + 1)
            seen[char] = right 
            length = max(length, right - left + 1)
        return(length)
