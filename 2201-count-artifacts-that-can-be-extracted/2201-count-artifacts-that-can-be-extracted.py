class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        excavated = set((r, c) for r, c in dig)
        res = 0
        for r1, c1, r2, c2 in artifacts:
            all_cells = [(r, c) for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)]
            if all(cell in excavated for cell in all_cells):
                res += 1
        return res