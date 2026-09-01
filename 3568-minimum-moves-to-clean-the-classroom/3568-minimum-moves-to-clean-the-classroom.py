class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m,n  = len(classroom),len(classroom[0])
        litters = {}
        dq = deque()
        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='S': dq.append((0,i,j,0))
                elif classroom[i][j]=='L': litters[(i,j)] = len(litters)
        if len(litters)==0: return 0 
        finalmask = (1<<len(litters))-1
        seen = [[[0]*(finalmask+1) for __ in range(n)] for __ in range(m)]
        seen[dq[0][1]][dq[0][2]][0]=energy
        while dq:
            moves,curx,cury,curmask= dq.popleft()
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nxtx,nxty = curx+dx,cury+dy
                if 0<=nxtx<m and 0<=nxty<n and classroom[nxtx][nxty]!='X':
                    nxtmask = curmask
                    nxtEnergy = seen[curx][cury][curmask]-1
                    if classroom[nxtx][nxty]=='L':
                        nxtmask = curmask | 1<<litters[(nxtx,nxty)]
                        if nxtmask==finalmask: return moves+1
                    elif classroom[nxtx][nxty]=='R':
                        nxtEnergy = energy
                    if seen[nxtx][nxty][nxtmask]>=nxtEnergy: continue
                    seen[nxtx][nxty][nxtmask]=nxtEnergy
                    if nxtEnergy==0: continue
                    dq.append((moves+1,nxtx,nxty,nxtmask))          
        return -1
                                        