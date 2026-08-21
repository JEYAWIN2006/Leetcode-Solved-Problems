class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> ans=new ArrayList<>();
        int t=1<<n;
        for(int j=0;j<t;j++){
            ans.add(j^(j>>1));
        }
        return ans;
    }
}