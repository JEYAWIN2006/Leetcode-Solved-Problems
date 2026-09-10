class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        res = mass
        for ast in asteroids:
            if ast > res:
                return False
            else:
                res += ast
        return True