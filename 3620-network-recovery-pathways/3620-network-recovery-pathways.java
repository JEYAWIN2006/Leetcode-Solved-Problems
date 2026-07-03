class Solution {
    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
        int n=online.length;
        List<List<int[]>> adj=new ArrayList<>();
        for(int i=0;i<n;i++){
             adj.add(new ArrayList<>());
        }
        int i=Integer.MAX_VALUE;
        int j=Integer.MIN_VALUE;
        for(int[] ed:edges){
            i=Math.min(i,ed[2]);
            j=Math.max(j,ed[2]);
            adj.get(ed[0]).add(new int[]{ed[1],ed[2]});
        }

        int res=-1;
        while(i<=j){
            int mid=i+(j-i)/2;
            if(isPossible(adj,mid,online,k)){
                res=mid;
                i=mid+1;
            }else{
                j=mid-1;
            }
        }

        return res;
    }

    private boolean isPossible(List<List<int[]>> adj,int cost,boolean[] online,long k){
        int n=online.length;
        Queue<long[]> q = new LinkedList<>();
        long[] c = new long[n];
        Arrays.fill(c,Long.MAX_VALUE);
        for(int[] nodes:adj.get(0)){
            int node = nodes[0], nodeCost = nodes[1];
            if(nodeCost >= cost && online[node]) {
                q.offer(new long[]{node,nodeCost,nodeCost});
                c[node]=nodeCost;
            }
        }
        while(!q.isEmpty()){
            long[] curr=q.poll();
            int node=(int) curr[0], currCost = (int) curr[2];
            long sum=curr[1];
            if(node==n-1 && sum<= k){
                return true;
            }
            if(c[node]<sum){
                continue;
            }
            for(int[] nei:adj.get(node)){
                int neiNode=nei[0], neiCost = nei[1];
                if(neiCost<cost){
                    continue;
                }
                long newCost = sum+neiCost;
                if(newCost>k || c[neiNode]<newCost || !online[neiNode]){
                    continue;
                }
                q.offer(new long[]{neiNode,newCost,neiCost});
                c[neiNode]=newCost;
            }
        }

        return false;
    }
}