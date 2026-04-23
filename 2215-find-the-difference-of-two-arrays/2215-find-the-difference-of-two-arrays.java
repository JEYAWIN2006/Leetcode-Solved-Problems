class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1=new HashSet<>();
        Set<Integer> set2=new HashSet<>();
        for(int n1:nums1){
            set1.add(n1);
        }
        for (int n2:nums2) {
            set2.add(n2);
        }
        List<Integer> list1=new ArrayList<>();
        List<Integer> list2=new ArrayList<>();
        for(int n1:set1){
            if(!set2.contains(n1)){
                list1.add(n1);
            }
        }
        for(int n2:set2){
            if (!set1.contains(n2)) {
                list2.add(n2);
            }
        }
        return List.of(list1, list2);
    }
}