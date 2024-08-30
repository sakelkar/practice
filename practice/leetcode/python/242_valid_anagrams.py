#https://leetcode.com/problems/valid-anagram/description/
from typing import Counter

class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        s_map = {}

        if len(s) != len(t):
            return False

        for c in s:
            s_map[c] += 1

        for c in t:
            if not c in s_map or s_map[c] == 0:
                return False
            s_map[c] -= 1

        return True

    def validAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        c_s = Counter(s)
        c_t = Counter(t)

        return c_s == c_t

    def validAnagram3(self, s: str, t: str):
        if len(s) != len(t):
            return False

        count = [0] * 26 

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return all(x == 0 for x in count)
         
