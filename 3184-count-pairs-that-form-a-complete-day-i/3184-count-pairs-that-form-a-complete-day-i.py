class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n = len(hours)
        count = 0
        for a in range(n):
            for b in range(a+1, n):
                if (hours[a] + hours[b]) % 24 == 0:
                    count = count + 1

        return count

        