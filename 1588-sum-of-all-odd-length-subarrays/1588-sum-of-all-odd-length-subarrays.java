class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int res=0;
        int n=arr.length;
        for(int i=0;i<n;i++)
        {
           int e=i+1; 
           int s=n-i;
           int tot=e*s;
           int o=tot/2;
           if(tot%2!=0){
            o++;
           }
           res+=o*arr[i];
        } 
        return res;
    }
}