class Solution {
    public int maxProduct(int[] nums) {
        int n=nums.length;
        if(n<2){
            return -1;
        }
        int m=Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int pro=(nums[i]-1)*(nums[j]-1);
                m=Math.max(m,pro);
            }
        }
        return m;
    }
}