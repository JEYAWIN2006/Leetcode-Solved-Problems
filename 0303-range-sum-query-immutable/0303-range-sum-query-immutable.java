class NumArray {
    private int[] p;
    public NumArray(int[] nums) {
        int n=nums.length;
        p=new int[n+1];
        p[0]=0;
        for(int i = 1;i<=n;i++){
            p[i]=p[i-1]+nums[i-1];
        }    
    }
    
    public int sumRange(int left, int right) {
        return p[right+1]-p[left];
    }
}