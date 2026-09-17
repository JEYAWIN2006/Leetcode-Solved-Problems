class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        count = 1
        curr = s[0]
        for i in s[1:]:
            if i == curr:
                count += 1
            else:
                if count == k:
                    return True
                else:
                    count = 1
                    curr = i

        return count == k

            