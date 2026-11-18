class Solution {
    public int minimumCardPickup(int[] cards) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        int mini=Integer.MAX_VALUE;
        for(int i=0;i<cards.length;i++){
            if(hm.containsKey(cards[i])){
                mini=Math.min(mini,i-hm.get(cards[i])+1);
            }
            hm.put(cards[i],i);
        }
        return mini==Integer.MAX_VALUE?-1:mini;
    }
}