class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        int[] a = new int[n + 1];
        a[n] = 0;

        for (int i = n - 1; i >= 0; i--) {
            a[i] = Integer.MIN_VALUE;
            int sum = 0;

            for (int k = 0; k < 3 && i + k < n; k++) {
                sum += stoneValue[i + k];
                a[i] = Math.max(a[i], sum - a[i + k + 1]);
            }
        }

        if (a[0] > 0)
            return "Alice";
        else if (a[0] < 0)
            return "Bob";
        else
            return "Tie";
    }
}