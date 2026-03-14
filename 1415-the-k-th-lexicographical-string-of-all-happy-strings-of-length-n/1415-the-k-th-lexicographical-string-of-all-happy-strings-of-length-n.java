class Solution {
    String result;
    int index=0;
    public String getHappyString(int n, int k) {
        dfs(new StringBuilder(), n, k);
        return result == null ? "" : result;
    }
    public void dfs(StringBuilder sbr, int n, int k) {
        if (n == 0) {
            index++;
            if (k == index) {
                result = sbr.toString();
            }
            return;
        }
        for (char c = 'a'; c <= 'c'; c++) {
            if (sbr.length() > 0 && sbr.charAt(sbr.length() - 1) == c) {
                continue;
            } 
            sbr.append(c);
            dfs(sbr, n - 1, k);
            sbr.deleteCharAt(sbr.length() - 1);
        }
    }
}