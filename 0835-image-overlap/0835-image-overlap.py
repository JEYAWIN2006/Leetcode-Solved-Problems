class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def check(di, dj):
            ctn = 0

            for i in range(n):
                for j in range(n):
                    if 0 <= i + di < n and 0 <= j + dj < n \
                            and img1[i][j] == img2[i + di][j + dj] == 1:
                        ctn += 1

            return ctn

        n = len(img1)
        ans = 0

        for i in range(-(n - 1), n):
            for j in range(-(n - 1), n):
                ctn = check(i, j)
                ans = max(ans, ctn)

        return ans