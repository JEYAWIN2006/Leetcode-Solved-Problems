class Solution:
    def minimumPushes(self, word: str) -> int:
        res, press = 0, 0
        for idx, (_, count) in enumerate(sorted(Counter(word).items(), key=lambda z: z[1])[::-1]):
            if idx % 8 == 0:
                press += 1
            res += count * press
        return res