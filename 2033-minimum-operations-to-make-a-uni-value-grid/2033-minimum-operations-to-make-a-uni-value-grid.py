class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n = len(grid[0])
        m = len(grid)
        length = m * n
        r = grid[0][0] % x
        grid = [grid[i][j] for i in range(m) for j in range(n)]
        for i in range(length):
            if grid[i] % x != r:
                return -1
            grid[i] = (grid[i] - r)//x
        grid.sort()

        @lru_cache
        def cal(x):
            total = 0
            for i in range(length):
                total += abs(x - grid[i])
            return total

        lo = min(grid)
        hi = max(grid)
        cur = lo
        step = max((lo + hi)//2, 1)
        res = cal(lo)
        while step >= 1:
            while res > cal(cur + step):
                res = cal(cur + step)
                cur += step
            while res > cal(cur - step):
                res = cal(cur - step)
                cur -= step
            step //= 2
        return res
        