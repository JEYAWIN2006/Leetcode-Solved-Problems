class Solution {
    public int maxProduct(int n) {
        char[] digits = Integer.toString(n).toCharArray();
        Arrays.sort(digits);
        int l=digits.length;
        int m1=digits[l-1]-'0';
        int m2=digits[l-2]-'0';
        return m1*m2;
    }
}