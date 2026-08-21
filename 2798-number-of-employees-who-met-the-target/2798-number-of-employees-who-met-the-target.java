class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int c=0;
        for(int p:hours){
            if(p>=target){
                c++;
            }
        }
        return c;
    }
}