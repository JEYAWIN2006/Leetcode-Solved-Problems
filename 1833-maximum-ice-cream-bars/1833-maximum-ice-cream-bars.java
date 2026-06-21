class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);
        int n=costs.length;
        int count=0;
        for(int i=0;i<n;i++){
            if(costs[i]<=coins){
                coins=coins-costs[i];
                count++;
            }
            else{
                break;
            }
        }
        return count;
    }
}