class Solution {
    public int sumOfEncryptedInt(int[] nums) {

        int rez = 0;

        for (int num : nums) {
            rez += encrypt(num);
        }

        return rez;
    }

    private int encrypt(int num) {

        int max = 0;
        int count = 0;
        int rez = 0;

        while (num > 0) {
            int tmp = num % 10;

            if (max < tmp) {
                max = tmp;
            }

            num /= 10;
            count++;
        }

        while (count > 0) {
            rez = rez * 10 + max;
            count--;
        }

        return rez;
    }
}