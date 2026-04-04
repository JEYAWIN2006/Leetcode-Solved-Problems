class Solution {
    public int evenNumberBitwiseORs(int[] nums) {
        int n=nums.length;
        int count=0;
        for(int num:nums){
            if(num%2==0){
                count=count|num;
            }
        }
        return count;
    }
}