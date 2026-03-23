class Solution {
    public int[] sortArray(int[] nums) {
        int n=nums.length;
        Arrays.sort(nums);
        int [] sorted=new int[n];
        for(int i=0;i<n;i++){
            sorted[i]=nums[i];
        }
        return sorted;
    }
}