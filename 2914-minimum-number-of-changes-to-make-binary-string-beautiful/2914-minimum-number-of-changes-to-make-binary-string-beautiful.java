class Solution {
    public int minChanges(String s) {
        int count = 0;

        for(int i = 0; i < s.length() - 1; i += 2) {
            int a = s.charAt(i) - '0';
            int b = s.charAt(i + 1) - '0';

            if(a != b) count++;
        }

        return count;
    }
}