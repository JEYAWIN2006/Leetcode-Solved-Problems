class Solution {
    public int alternateDigitSum(int n) {
        String s = String.valueOf(n);
        int sum = 0;
        boolean t = true;
        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if(t){
                sum = sum + (ch-'0');
                t = false;
            }
            else {
                sum = sum - (ch-'0');
                t = true;
            }
        }
        return sum;
    }
}