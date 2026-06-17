class Solution {
    public int sumofdig(int num){
        int sum=0;
        while(num>0){
            sum+=num%10;
            num/=10;
        }
        return sum;
    }

    public int minElement(int[] nums) {
        int mini=Integer.MAX_VALUE;
        for(int i=0;i<nums.length;i++){
            int k=sumofdig(nums[i]);
            if(k<mini){
                mini=k;
            }
        }
        return mini;
    }
}