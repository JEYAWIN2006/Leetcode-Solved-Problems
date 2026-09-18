import heapq
from collections import defaultdict


class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        R, C = len(matrix), len(matrix[0])
        
        teleport = defaultdict(list)

        for r in range(R):
            for c in range(C):
                if (matrix[r][c] == '.' or 
                    matrix[r][c] == '#'):
                    continue
                teleport[matrix[r][c]].append((r, c))
        
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        heap = [(0, 0, 0)]
        
        seen = set([(0, 0)])

        if matrix[0][0] not in {'.', '#'}:
            for r, c in teleport[matrix[0][0]]:
                seen.add((r, c))
                heapq.heappush(heap, (0, r, c))

        while heap:
            moves, r, c = heapq.heappop(heap)

            if r == R - 1 and c == C - 1:
                return moves
            
            for dr, dc in DIRECTIONS:
                fr, fc = r + dr, c + dc
                if (0 <= fr < R and
                    0 <= fc < C and
                    matrix[fr][fc] != '#' and
                    (fr, fc) not in seen):
                    if matrix[fr][fc] != '.':
                        for ar, ac in teleport[matrix[fr][fc]]:
                            if (ar, ac) not in seen:
                                seen.add((ar, ac))
                                heapq.heappush(heap, (moves+1, ar, ac))
                        continue
                    seen.add((fr, fc))
                    heapq.heappush(heap, (moves + 1, fr, fc))
        
        return -1
        