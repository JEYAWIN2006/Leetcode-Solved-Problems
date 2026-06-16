import java.util.*;
class Solution {
    public int[] leftRightDifference(int[] nums) {
         int[] ans=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            int sum=0;
            int sum2=0;
            for(int j=i;j<nums.length;j++){
                sum+=nums[j];
            }
            for(int j=i;j>=0;j--){
                sum2+=nums[j];
            }
            ans[i]=Math.abs(sum-sum2);

        }
    return ans;
    }
}
