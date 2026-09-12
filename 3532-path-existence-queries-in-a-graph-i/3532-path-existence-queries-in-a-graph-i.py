class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        prefix = [0] * n

        for i in range(1, n):
            gap = 1 if (nums[i] - nums[i - 1]) > maxDiff else 0
            prefix[i] = prefix[i - 1] + gap

        return [prefix[u] == prefix[v] for u, v in queries]