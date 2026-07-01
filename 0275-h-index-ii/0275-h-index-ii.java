class Solution {
    public int hIndex(int[] citations){
        int left=0;
        int n=citations.length;
        int right=n-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            int rem=n-mid;
            if(citations[mid]==rem){
            return rem;
            }
            else if(citations[mid]>rem){
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }
        
        return n-left;
    }
}
