class Solution {
    public int trailingZeroes(int n) {
        int count=0;
        if(n==0){
            return 0;
        }
       while(n>=5){
        n/=5;
        count+=n;
       }
       return count;
    }
}