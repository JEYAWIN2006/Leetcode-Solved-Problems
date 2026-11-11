class Solution:
    def numEquivDominoPairs(self, a: List[List[int]]) -> int:
        return sum(f*(f-1)//2 for f in Counter(min(p)*10+max(p) for p in a).values())