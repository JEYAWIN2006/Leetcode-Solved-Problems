class Solution {
    public int longestSubsequence(int[] nums) {
        boolean nz=false;
        int x=0;
        for(int i:nums){
            x^=i;
            if(i>0){
                nz=true;
            }
        }
        if(!nz){
            return 0;
        }
        if(x==0){
            return nums.length-1;
        }
        return nums.length;
    }
}