#https://leetcode.com/problems/longest-palindromic-substring/

#Given a string s, return the longest palindromic substring in s.
class Solution:
    #Brute Force Approach O(N^3)
    def longestPalindromicSubstring(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if s[i:j] == s[i:j][::-1]:
                    if len(answer) < len(s[i:j]):
                        answer = s[i:j]
        return(answer)

    def longestPalindromicSubstring2(self, s: str) -> str:
        answer = ""
        answerLen = 0
        for i in range(len(s)):
            #odd length
            left, right = i, i 
            while left >= 0 and right <= len(s) and s[left] == s[right]:
                if answerLen < (right - left + 1):
                    
                    answer = s[left:right+1]
                    answerLen = right - left + 1 
                left -= 1
                right += 1

            #even length
            left, right = i, i+1 
            while left >= 0 and right <= len(s) and s[left] == s[right]:
                if answerLen < (right - left + 1):
                    answer = s[left:right+1]
                    answerLen = right - left + 1
                left -= 1
                right += 1
        return(answer)


class Solution2:
    def longestPalindromicSubstring(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if s[i:j] == s[i:j][::-1]:
                    if len(answer) < len(s[i:j]):
                        answer = s[i:j+1]
        return(answer)

    def longestPalindromicSubstring2(self, s: str) -> str:
        answer = ""
        answerLen = 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if answerLen < right - left + 1:
                    answer = s[left:right+1]
                    answerLen = right - left + 1
                left -= 1
                right += 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if answerLen < right - left + 1:
                    answer = s[left:right+1]
                    answerLen = right - left + 1
                left -= 1
                right += 1
        return(answer)




