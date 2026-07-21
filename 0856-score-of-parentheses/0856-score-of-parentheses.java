class Solution {
    public int scoreOfParentheses(String s) {
        int count=0;
        int st=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('){
                count++;
                continue;
            }
            count--;
            if(s.charAt(i-1)=='('){
                st=st+(1<<count);
            }
        }
        return st;
    }
}