class Solution {

    int MOD = 1000000007;
    Integer[][][][] memo;

    public int numberOfStableArrays(int zero, int one, int limit) {
        memo = new Integer[zero+1][one+1][2][limit+1];
        return backtrack(zero, one, limit, -1, 0);
    }
    public int backtrack(int zero, int one, int limit, int last, int length) {
        if (zero == 0 && one == 0) return 1;
        if (last != -1 && memo[zero][one][last][length] != null)
            return memo[zero][one][last][length];
        int ans = 0;
        if (zero > 0) {
            if (last != 0 || length < limit) {
                int newLen = (last == 0) ? length + 1 : 1;
                ans = (ans+backtrack(zero - 1, one, limit, 0, newLen)) % MOD;
            }
        }

        if (one > 0) {
            if (last != 1 || length < limit) {
                int newLen = (last == 1) ? length + 1 : 1;
                ans = (ans+backtrack(zero, one - 1, limit, 1, newLen)) % MOD;
            }
        }
        if (last != -1)
            memo[zero][one][last][length] = ans;

        return ans;
    }
}