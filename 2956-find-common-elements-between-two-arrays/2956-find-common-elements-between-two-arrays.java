class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        boolean[] array1 = new boolean[101];
        boolean[] array2 = new boolean[101];
        for (int num : nums1) {
            array1[num] = true;
        }
        for (int num : nums2) {
            array2[num] = true;
        }
        int answer1 = 0;
        int answer2 = 0;
        for (int num : nums1) {
            if (array2[num]) {
                answer1++;
            }
        }
        for (int num : nums2) {
            if (array1[num]) {
                answer2++;
            }
        }
        int[] result = {answer1, answer2};
        return result;
    }
}