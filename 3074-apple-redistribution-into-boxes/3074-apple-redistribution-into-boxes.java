class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        int sum = 0;
        for(int i=0;i<apple.length;i++){
            sum+=apple[i];
        }
        Arrays.sort(capacity);
        int count = 0;
        int count1 = 0;
        for(int i=capacity.length-1;i>=0;i--){
            if(count>=sum){
                break;
            }
            count+=capacity[i];
            count1++;
        }
        return count1;
    }
}