class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = str(n).replace("0", "")

        if not digits:
            return 0

        x = int(digits)
        digit_sum = sum(map(int, digits))

        return x * digit_sum