class Solution {
    public boolean divideArray(int[] nums) {
        int [] j=new int[501];
        for(int num:nums){
            j[num]++;
        }
        for(int i=0;i<501;i++){
            if(j[i]%2!=0){
                return false;
            }
        }
        return true;
    }
}