class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n=matrix.length;
        for(int i=0;i<n;i++){
            int k=matrix[i].length;
            for(int j=0;j<k;j++){
                if(matrix[i][j]==target){
                    return true;
                }
            }
        }
    return false;
    }
}