class Solution {

    public long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    public int nthMagicalNumber(int n, int a, int b) {
        long g = gcd(a, b);
        long lcm = (a / g) * b;
        long left = 1;
        long right = (long) n * Math.min(a, b);
        while (left < right) {
            long mid = left + (right - left) / 2;
            long count = mid / a + mid / b - mid / lcm;
            if (count >= n) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return (int)(left % 1000000007);
    }
}