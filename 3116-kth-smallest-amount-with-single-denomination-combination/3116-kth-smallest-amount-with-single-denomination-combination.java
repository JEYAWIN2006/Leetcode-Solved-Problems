class Solution {
    public long findKthSmallest(int[] coins, int k) {
        long left = 1;
        // Adjusted to the absolute maximum potential answer: 25 * 2e9 = 50,000,000,000
        long right = 50_000_000_000L; 
        long ans = right;

        while (left <= right) {
            long mid = left + (right - left) / 2;
            if (check(mid, coins, k)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }

    private boolean check(long mid, int[] coins, int k) {
        int n = coins.length;
        long total = 0;

        for (int m = 1; m < (1 << n); m++) {
            long lcm = 1;
            int bitCount = 0;
            for (int j = 0; j < n; j++) {
                if ((m & (1 << j)) != 0) {
                    lcm = lcm(lcm, coins[j]);
                    if (lcm > mid) { // Stop early to avoid unnecessary computations
                        break;
                    }
                    bitCount++;
                }
            }
            if (lcm <= mid) {
                if (bitCount % 2 == 1) {
                    total += mid / lcm;
                } else {
                    total -= mid / lcm;
                }
            }
        }
        return total >= k;
    }

    private long lcm(long a, long b) {
        return (a / gcd(a, b)) * b;
    }

    private long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
