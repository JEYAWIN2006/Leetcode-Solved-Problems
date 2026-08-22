class Solution {
    public boolean checkDivisibility(int n) {
        int s=0;
        int p=1;
        int d=n;
        while(n>0){
            int r=n%10;
            s=s+r;
            p=p*r;
            n/=10;
        }
        int k=s+p;
        if(d%k==0){
            return true;
        }
        return false;
    }
}