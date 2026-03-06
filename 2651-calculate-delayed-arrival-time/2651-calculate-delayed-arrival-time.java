class Solution {
    public int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        int k=arrivalTime + delayedTime;
        if(k>23){
            return (k-24);
        }
       return k;
    }
}