class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder ans = new StringBuilder();
        int n=words.length;
        for(int i=0;i<n;i++){
            int j=0;
            int t=0;
            while(j<words[i].length()){
                int ch=words[i].charAt(j);
                t=(t+weights[ch-97])%26;
                j++;
            }
            char ch=(char)(122-t);
            ans.append(ch);

        }   
        return ans.toString();
    }
}