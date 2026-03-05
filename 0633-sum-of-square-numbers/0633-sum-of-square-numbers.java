class Solution {
    public boolean judgeSquareSum(int c) {
        for(long i=0;i*i<=c;i++){
            long j=c-(i*i);
            long k=(int)Math.sqrt(j);
            if(k*k==j){
                return true;
            }
        }
        return false;
    }
}