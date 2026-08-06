
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0 :
            return 1
        a = 10
        u = 9
        av = 9
        for i in range(2, n + 1):
            u *= av
            a += u
            av -= 1
        return a