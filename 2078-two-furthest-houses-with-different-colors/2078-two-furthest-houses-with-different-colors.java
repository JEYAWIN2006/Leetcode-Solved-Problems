class Solution {
    public int maxDistance(int[] colors) {
        int c=0;
        for(int i=0;i<colors.length-1;i++)
            for(int j=i+1;j<colors.length;j++)
                if(colors[i]!=colors[j])
                    c=Math.max(c,j-i);
        return c;
    }
}