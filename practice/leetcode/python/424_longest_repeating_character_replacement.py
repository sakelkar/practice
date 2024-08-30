#https://leetcode.com/problems/longest-repeating-character-replacement/description/
#You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#Return the length of the longest substring containing the same letter you can get after performing the above operations.
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
#
#Constraints:
#    1 <= s.length <= 105
#    s consists of only uppercase English letters.
#    0 <= k <= s.length

import collections
from typing import Counter
class Solution :
    def longestRepeatingCharReplacement2(self, s: str, k: int) -> int:
        ans = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                counts = Counter(s[i:j+1])
                for cnt in counts.values():
                    if (j - i + 1) - cnt <= k:
                        ans = max(ans, (j - i + 1))
        return ans

    def longestRepeatingCharReplacement(self, s: str, k: int) -> int:
        freqMap = collections.defaultdict(int) 
        p1 = max_length = max_freq = 0
            
        for p2, ch in enumerate(s):
            freqMap[ch] += 1
            max_freq = max(max_freq, freqMap[ch])

            while (p2 - p1 + 1) > max_freq + k:
                freqMap[s[p1]] -= 1
                p1 += 1

            max_length = max(max_length, p2 - p1 + 1)
        return max_length

    #keep increasing the window towards right until the size of the window = max_freq of the element in that window + k 
    #as soon as windows crosses that record the length of the max freq charateter such that it is 


    def longestRpeatingCharReplacement3(self, s: str, k: int)->int:
        map = {}
        l = 0
        max_len = 0
        max_f = 0
        for r in range(len(s)):
            map[s[r]] = 1 + map.get(s[r], 0)
            max_f = max(max_f, map[s[r]])

            while (r - l + 1) - max_f > k:
                map[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len


