class Solution {
    public int fibrec(int x){
        if(x==0){
            return 0;
        }
        if(x==1){
            return 1;
        }
        return fibrec(x-2)+fibrec(x-1);
    }
    public int fib(int n) {
        return fibrec(n);
    }
}