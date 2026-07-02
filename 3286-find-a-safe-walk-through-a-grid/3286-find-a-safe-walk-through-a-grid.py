

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m,n=len(grid),len(grid[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        queue=deque([(0,0,health-grid[0][0])])
        visited=set([(0,0,health-grid[0][0])])
        while queue:
            r,c,h=queue.popleft()
            if (r,c)==(m-1,n-1) and h > 0:
                return True
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n:
                    new=h-grid[nr][nc]
                    if new>0 and (nr,nc,new) not in visited:
                        visited.add((nr,nc,new))
                        queue.append((nr,nc,new))
        return False
      