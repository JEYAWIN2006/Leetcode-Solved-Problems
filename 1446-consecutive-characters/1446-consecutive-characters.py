class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(list(b)) for a, b in itertools.groupby(s))