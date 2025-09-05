#Given a string s, return the longest in s.

#Example 1:
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.

#Example 2:
#Input: s = "cbbd"
#Output: "bb"

#Constraints:
#    1 <= s.length <= 1000
#    s consist of only digits and English letters.
class Solution:
    def longestPalindromatic(self, s: str) -> str:
        answer = ""
        answerLen = 0

        if not s:
            return ""

        #babab
        #palindrome can be of odd length or even length so calculate for two possibilities
        #for odd length center is same so start left and right = i
        #for even start as left = i, right = i+1
        for i in range(len(s)):
            #odd
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if answerLen < (right - left + 1):
                    answer = s[left:right+1]
                    answerLen = answer
                left -= 1
                right += 1

            #even
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if answerLen < (right - left + 1):
                    answer = s[left:right+1]
                    answerLen = answer
                left -= 1
                right += 1

        return answer

    def longestPalindromatic2(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            #return adjusted left and right since you would have reversed left and right.
            return left + 1, right - 1

        for i in range(len(s)):
            #odd length
            l1, r1 = expand(i, i)
            #even length
            l2, r2 = expand(i, i+1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end+1]
