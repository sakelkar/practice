#https://www.lintcode.com/problem/659/
#Description
#Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#Please implement encode and decode

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        answer = ""
        for word in strs:
            answer =  str(len(word)) + '#' + word
        return answer

    def decode(self, string: str) -> List[str]:
        answer = []
        p1 = 0
        while p1 < len(string):
            p2 = p1
            while string[p2] != "#":
                p2 += 1

            word_len = int(string[p1:p2])
            answer.append(string[p2+1:p2+1+word_len])
            p1 = p2 + 1 + word_len
        return(answer)

