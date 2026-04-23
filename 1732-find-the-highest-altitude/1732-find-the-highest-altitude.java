class Solution {
    public int largestAltitude(int[] nums){
        int a=0;
        int m=0;
        for(int i=0;i<nums.length;i++){
            a+=nums[i];
            if(m<a){
                m=a;
            }
        }
        return m;
    }
}