class Solution {
    public int mirrorDistance(int n) {
        int og=n;
        int rev=0;
        int last=0;
        int ans=0;
        while(n!=0){
            last=n%10;
            rev=rev*10+last;
            n/=10;
        }
        ans=Math.abs(og-rev);
        return ans;
    }
}