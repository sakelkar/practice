#https://leetcode.com/problems/first-unique-character-in-a-string/solutions/

#Given a string s, find the first non-repeating character in it and return its index.
#If it does not exist, return -1
from typing import AnyStr 
class solution:
    def firstUniqueChar(self, s: AnyStr) -> int:
        charMap = {}
        for index, char in enumerate(s):
            if char in charMap:
                charMap[char] = -1
            else:
                charMap[char] = index

        for char in s:
            if charMap[char] != -1:
                return charMap[char]
        return -1
