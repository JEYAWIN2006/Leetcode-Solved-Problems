class Solution {
    public int numberOfSpecialChars(String word) {
        int [] up=new int[26];
        int [] low=new int[26];
        for(int i=0;i<word.length();i++)
        {
            char x=word.charAt(i);
            if(x>='A' && x<='Z')
            {
                int d=x-'A';
                if(low[d]==-1)
                {
                    continue;
                }
                if(low[d]==1)
                {
                    up[d]=1;
                }
                else
                {
                    up[d]=-1;
                    low[d]=-1;
                }
            }
            else
            {
                int d=x-'a';
                if(low[d]==-1)
                {
                    continue;
                }
                if(up[d]==1)
                {
                    low[d]=-1;
                    up[d]=-1;
                }
                else
                {
                    low[d]=1;
                }
            }
        }
        int count=0;
        for(int i=0;i<26;i++)
        {
            if(up[i]==1 && low[i]==1)
            {
                count++;
            }
        }
        return count;
    }
}