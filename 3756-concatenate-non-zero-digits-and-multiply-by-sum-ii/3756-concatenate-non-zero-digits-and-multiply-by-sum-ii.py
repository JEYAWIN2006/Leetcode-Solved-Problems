class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = int(1e9 + 7)
        n = len(s)
        Pow = [1 for _ in range(100001)]

        for i in range(1, 100001):
            Pow[i] = (Pow[i - 1] * 10) % mod

        pre_count = [0 for _ in range(n)]
        pre_sum = [0 for _ in range(n)]
        pre_num = [0 for _ in range(n)]

        pre_count[0] = 1 if s[0] != '0' else 0
        pre_sum[0] = pre_num[0] = int(s[0])

        for i in range(1, n):
            pre_count[i] = pre_count[i - 1] + 1 if s[i] != '0' else pre_count[i - 1]
            pre_sum[i] = (pre_sum[i - 1] + int(s[i])) % mod
            pre_num[i] = ((pre_num[i - 1] * 10) % mod + int(s[i])) % mod if s[i] != '0' else pre_num[i - 1]

        q = len(queries)
        ans = [0 for _ in range(q)]
        for i in range(q):
            l, r = queries[i]

            if l == 0:
                ans[i] = (pre_num[r] * pre_sum[r]) % mod
            else:
                Count = (pre_count[r] - pre_count[l - 1] + mod) % mod
                Sum = (pre_sum[r] - pre_sum[l - 1] + mod) % mod
                Num = (pre_num[r] - (pre_num[l - 1] * Pow[Count]) % mod + mod) % mod

                ans[i] = (Num * Sum) % mod
        
        return ans