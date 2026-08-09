class Solution {
    public int smallestEvenMultiple(int n) {
        int lcm=0;
        if(n%2==0){
            lcm=n;
        }
        else{
            lcm=n*2;
        }
        return lcm;
    }
}