class Solution {
    public int minOperations(int[] nums, int k) {
        int c=0;
        for(int i:nums){
            if(i<k){
                c++;
            }
        }
        return c;
    }
}