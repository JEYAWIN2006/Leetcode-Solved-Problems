class Solution {
public:
    int beautifulSplits(vector<int>& nums) {
        int ret = 0;
        int n = nums.size();
        for(int i = 1; i < n-1; i++){
            for(int j = i+1; j < n; j++){
                bool fl1 = (j - i >= i) && equal(nums.begin(), nums.begin() + i, nums.begin() + i);
                if(fl1){
                    ret += (n-j);
                    break;
                }
                bool fl2 = (n - j >= j - i) && equal(nums.begin() + i, nums.begin() + j, nums.begin() + j);
                if (fl2) 
                    ret++;                
            }
        }
        return ret;   
    }
};