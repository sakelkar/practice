#https://leetcode.com/problems/longest-common-prefix/

#Write a function to find the longest common prefix string amongst an array of strings
#If there is no common prefix, return an empty string ""
from typing import List

class Solution:
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        answer = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] == strs[0][i]:
                    return(answer)
            answer += strs[0][i]
        return answer

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        answer = ""
        for i in range(min_len):
            curr_char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != curr_char:
                    return answer
            answer += curr_char
        return(answer)
