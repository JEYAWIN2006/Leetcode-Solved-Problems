class Solution:
    def minimumCost(self, cost: list[int]) -> int:

        n, s = len(cost), sum(cost)
        cost.sort(reverse = True)
        return s - sum(cost[2:n:3])
            