class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int j=0;
        for(int i=0;i<arr2.length;i++){
            for(int k=j;k<arr1.length;k++){
                if(arr1[k]==arr2[i]){
                    int temp=arr1[j];
                    arr1[j]=arr1[k];
                    arr1[k]=temp;
                    j++;
                }
            }
        }
        Arrays.sort(arr1,j,arr1.length);
        return arr1;
    }
}