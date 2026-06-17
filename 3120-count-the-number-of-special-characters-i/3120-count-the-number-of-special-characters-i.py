class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        un=set(word)
        for i in range(26):
            lower=chr(ord('a')+i)
            upper=chr(ord('A')+i)
            if lower in un and upper in un:
                count=count+1
        return count