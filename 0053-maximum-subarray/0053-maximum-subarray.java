class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int m = Integer.MIN_VALUE;
        int sum = 0;
        for (int s = 0; s < n; s++) {
            sum += nums[s];
            if (sum > m) {
                m = sum;
            }
            if (sum < 0) {
                sum = 0;
            }
        }

        return m;
    }
}