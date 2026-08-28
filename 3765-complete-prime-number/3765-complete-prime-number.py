class Solution:
    def completePrime(self, num: int) -> bool:

        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5)+1, 2):
                if n % i == 0:
                    return False
            return True

        string = str(num)

        for i in range(len(string)):
            prefix = string[:i+1]
            suffix = string[i:]

            x = int(prefix)
            y = int(suffix)

            if not is_prime(x) or not is_prime(y):
                return False

        return True