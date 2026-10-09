class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(1, 3):
                cnt_w = 0
                for di, dj in [(0, 0), (0, -1), (1, 0), (1, -1)]:
                    if grid[i + di][j + dj] == "W": cnt_w += 1
                if cnt_w != 2: return True
        return False