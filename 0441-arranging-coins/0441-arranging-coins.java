class Solution {
    public int arrangeCoins(int n) {
        int result=n/2+1,num=n;
        for(int i=1;i<=n;i++){
            num-=i;
            if(num<0){
                return i-1;
            }
            if(num==0){
                return i;
            }
        }
        return -1;
    }
}