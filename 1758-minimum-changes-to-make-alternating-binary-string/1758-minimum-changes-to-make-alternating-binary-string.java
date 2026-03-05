class Solution {
    public int minOperations(String s) {
        int n=s.length();
        int s1=0;
        int s2=0;
        for(int i=0;i<n;i++){
            if(i%2==0){
                if(s.charAt(i)=='0'){
                    s2++;
                }
                else{
                    s1++;
                }
            }
            else{
                if(s.charAt(i)=='1'){
                    s2++;
                }
                else{
                    s1++;
                }
            }
        }
        int k=Math.min(s1,s2);
        return k;
    }
}