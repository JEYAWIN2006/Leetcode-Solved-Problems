class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.length;
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i][0] = nums[i];
            pairs[i][1] = i;
        }
        java.util.Arrays.sort(pairs, (a, b) -> Integer.compare(a[0], b[0]));
        int[] result = new int[n];
        int left = 0;
        while (left < n) {
            int right = left;
            while (right + 1 < n && pairs[right + 1][0] - pairs[right][0] <= limit) {
                right++;
            }
            int len = right - left + 1;
            int[] indices = new int[len];
            for (int i = 0; i < len; i++) {
                indices[i] = pairs[left + i][1];
            }
            java.util.Arrays.sort(indices);
            for (int i = 0; i < len; i++) {
                result[indices[i]] = pairs[left + i][0];
            }

            left = right + 1;
        }

        return result;
    }
}