class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        x=[[-1]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    x[i][j]=j
                elif j==0:
                    x[i][j]=i
                elif word1[i-1] == word2[j-1]:
                    x[i][j]=x[i-1][j-1]
                else:
                    x[i][j] = min(x[i-1][j], x[i][j-1], x[i-1][j-1]) + 1
        return x[m][n]

