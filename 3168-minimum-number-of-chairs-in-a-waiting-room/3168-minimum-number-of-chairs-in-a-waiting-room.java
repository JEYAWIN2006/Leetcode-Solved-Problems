class Solution {
    public int minimumChairs(String s) {
        int chairs=0;
        int res=0;
        for(int i=0;i<s.length();i++){
            if(chairs==0 && s.charAt(i)=='E'){
                res++;
            }
            else if(chairs>0 && s.charAt(i)=='E'){
                chairs-=1;
            }
            else if(s.charAt(i)=='L'){
                chairs++;
            }
        }
        return res;
    }
}