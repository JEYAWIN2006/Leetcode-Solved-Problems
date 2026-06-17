class Solution {
    public int sumOfGoodNumbers(int[] nums, int k) {
        int sum=0;
        for(int i=0;i<k;i++){
            if(nums[i]>nums[i+k]){
                sum+=nums[i];
            }
        }
        for(int i=k;i<nums.length-k;i++){
            if(nums[i]>nums[i-k] && nums[i]>nums[i+k]){
                sum+=nums[i];
            }
        }
        for(int i=nums.length-k;i<nums.length;i++){
            if(nums[i]>nums[i-k]){
                sum+=nums[i];
            }
        }
        return sum;
    }
}