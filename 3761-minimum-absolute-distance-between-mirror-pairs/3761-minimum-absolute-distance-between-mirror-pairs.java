class Solution {
    public int minMirrorPairDistance(int[] nums) {
        int n = nums.length;
        int res = Integer.MAX_VALUE;
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i<n; i++){
            int curr = nums[i];
            int temp = curr;
            int rev = 0;
            while(temp > 0){
                int last = temp % 10;
                temp /= 10;
                rev = rev * 10 + last;
            }

            if(map.containsKey(curr) && i > map.get(curr)){
                res = Math.min(res, Math.abs(i - map.get(curr)));
            }
            map.put(rev, i);
        }
        return res == Integer.MAX_VALUE ? -1 : res;
    }
}