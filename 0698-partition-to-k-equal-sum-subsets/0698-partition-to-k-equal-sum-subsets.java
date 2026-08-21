class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0;
        int n = nums.length;
        for(int i = 0 ; i < n ; i++){
            sum += nums[i];
        }
        int max = 0;
        for(int x:nums)max=Math.max(max,x);
        if(sum % k != 0 || max > sum/k){
            return false;
        }
        sum = sum/k;
        int[] ss = new int[k];
        Arrays.sort(nums);
        return helper(nums,ss,k,n-1,sum);
    }
    
    public boolean helper(int[] arr,int[] ss, int k, int n, int target){
        if(n == -1){
            for(int x : ss){
                if(x != target){
                    return false;
                }
            }
            return true;
        }
        
        for(int i = 0; i < k ; i++){
            if(i-1>=0 && ss[i-1]==0)break;
            if(arr[n] + ss[i] <= target){
                ss[i] += arr[n];
                if(helper(arr,ss,k,n-1,target))return true;
                ss[i] -= arr[n];
            }
        }
        return false;
    }
}