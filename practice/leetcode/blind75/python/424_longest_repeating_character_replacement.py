#You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#
#Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
#Example 1:
#
#Input: s = "ABAB", k = 2
#Output: 4
#Explanation: Replace the two 'A's with two 'B's or vice versa.
#
#Example 2:
#
#Input: s = "AABABBA", k = 1
#Output: 4
#Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
#The substring "BBBB" has the longest repeating letters, which is 4.
#There may exists other ways to achieve this answer too.

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = 0
        maxCount = 0
        maxLength = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            freq[index] += 1

            maxCount = max(maxCount, freq[index])
            #if current window length - maxFrequency in the current windo is > k then we have invalid window and we need move left
            if right - left + 1 - maxCount > k:
                #reduce the frequency of character at left by 1
                freq[ord(s[left]) - ord('A')] -= 1
                #increment the left pointer
                left += 1

            maxLength = max(maxLength, right - left + 1)
        return maxLength

    def characterReplacement2(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        #freq = [0] * 26
        left = 0
        maxLength = 0
        maxFreq = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            freq[index] += 1

            maxFreq = max(maxFreq, freq[index])
            if right - left + 1 - maxFreq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)
        return maxLength

