class Solution {
    public int maxProduct(int n) {
        int maxpro=0;
        String digits=String.valueOf(n);
        for(int i=0;i<digits.length();i++) {
            for(int j=i+1;j<digits.length();j++) {
                int d1=digits.charAt(i)-'0';
                int d2=digits.charAt(j)-'0';
                int pro=d1*d2;
                maxpro=Math.max(maxpro,pro);
            }
        }
        
        return maxpro;
    }
}