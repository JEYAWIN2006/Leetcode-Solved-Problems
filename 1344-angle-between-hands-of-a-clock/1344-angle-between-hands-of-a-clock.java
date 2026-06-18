class Solution {
    public double angleClock(int hour, int minutes) {
        int h=(hour%12);
        int mang=minutes*6;
        double hang=(h*30)+(minutes*0.5);
        double ang= Math.abs(mang-hang);
        if(ang>=180){
            return 360-ang;
        }
        return ang;
    }
}