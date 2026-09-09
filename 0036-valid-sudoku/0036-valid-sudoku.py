class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = []
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele != '.':
                    r += [(i, ele), (ele, j), (i // 3, j // 3, ele)]
        return len(r) == len(set(r))