#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

#28. Find the Index of the First Occurrence in a String
#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
#or -1 if needle is not part of haystack.

from typing import List

class Solution:
    def buildLPS(self, needle: str) -> List[int]:
        if len(needle) == 0:
            return []

        prevLPS, i = 0, 1
        lps = [0]*len(needle)
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        return(lps)

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 or len(haystack) == 0:
            return(-1)

        i = 0
        j = 0
        lps = self.buildLPS(needle)
        while i < len(haystack):
            if needle[j] == haystack[i]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return(i - len(needle))
        return(-1)


class Solution2:
    def buildLPS(self, needle: str) -> List[int]:
        if len(needle) == 0:
            return []

        prevLPS, i = 0, 1
        lps = [0] * len(needle)

        while(i < len(needle)):
            if needle[i] == needle[prevLPS]:
                lps[i++] == ++prevLPS
            elif prevLPS == 0:
                lps[i++] = 0
            else:
                prevLPS = lps[prevLPS - 1]

        return(lps)

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 or len(haystack) == 0:
            return -1
        i, j = 0, 0
        lps = self.buildLPS(needle)
        while (i < len(haystack)):
            if needle[j] == haystack[i]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == len(needle):
                return(i - len(needle))
        return(-1)
