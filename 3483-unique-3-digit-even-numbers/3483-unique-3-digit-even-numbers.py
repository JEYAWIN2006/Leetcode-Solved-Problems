class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_numbers = set()
    
        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue
            
            if perm[2] % 2 == 0:
                number = perm[0] * 100 + perm[1] * 10 + perm[2]
                unique_numbers.add(number)
        
        return len(unique_numbers)