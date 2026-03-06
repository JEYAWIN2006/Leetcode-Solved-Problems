class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        String[] n1 = num1.replace("i", "").split("\\+");
        String[] n2 = num2.replace("i", "").split("\\+");
        int a = Integer.parseInt(n1[0]); 
        int b = Integer.parseInt(n1[1]);  
        int c = Integer.parseInt(n2[0]);  
        int d = Integer.parseInt(n2[1]);
        int realPart = a * c - b * d;
        int imagPart = a * d + b * c;
        return realPart + "+" + imagPart + "i";
    }
}