class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] arr=s.toCharArray();
        int n=arr.length;
        int maxlen=0;
        int[] last=new int[128];
        for(int i=0;i<128;i++){
            last[i]=-1;
        }
        int l=0;
        for(int r=0;r<n;r++){
            char curr=arr[r];
            if(last[curr]>=l){
                l=last[curr]+1;
            }
            last[curr]=r;
            maxlen=Math.max(maxlen,r-l+1);
        }
        return maxlen;
    }
}