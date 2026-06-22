class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for word in sentences:
            k=word.split()
            j=len(k)
            if j>m:
                m=j
        return m
