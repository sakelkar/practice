#Given two strings s and t, return true if t is an
#of s, and false otherwise.
#
#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true
#
#Example 2:
#Input: s = "rat", t = "car"
#Output: false
#
#Constraints:
#    1 <= s.length, t.length <= 5 * 104
#    s and t consist of lowercase English letters.
#Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #define a map where the character is key and its occurance is its value
        #first compare the length of s and t and they HAVE to be equal otherwise return immediately

        #best question to get clarified about is capital A and small a are considered equal
        #assuming that all letters are small letters then solution becomes more simple.
        if len(s) != len(t):
            return False

        count = [] * 26#assuming all are small letters
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            count[ord(ch) - ord('a')] -=1
            if count[ord(ch) - ord('a')] < 0:
                return False

        return True

    def isAnagram1(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)



