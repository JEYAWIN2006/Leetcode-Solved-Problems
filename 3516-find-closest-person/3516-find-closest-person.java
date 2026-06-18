class Solution {
    public int findClosest(int x, int y, int z) {
        int k=Math.abs(x-z);
        int j=Math.abs(y-z);
        if(k<j){
            return 1;
        }
        else if(k>j){
            return 2;
        }
        return 0;
    }
}