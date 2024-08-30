#https://leetcode.com/problems/valid-anagram/description/

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
