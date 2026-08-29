class Solution {
    public int[][] generateMatrix(int n) {
        if(n==1) return new int[][]{{1}};
        int [][] ans=new int[n][n];
        int i=0;
        int j=0;
        int dir=0;
        int xbound=0;
        int ybound=0;
        int row=n-1;
        int col=n-1;
        int temp=n*n+1;
        int ind=1;
        while(temp!=ind){
            if(dir==0){
                ans[i][j++]=ind++;;
                if(j==col+1 && i==xbound){
                    dir=1;
                    xbound++;
                    i++;
                    j--;
                }
            }
            else if(dir==1){
                ans[i++][j]=ind++;;
                if(i==row+1 && j==col){
                    dir=2;
                    col--;
                    j--;
                    i--;
                }
            }
            else if(dir==2){
                ans[i][j--]=ind++;;
                if(i==row && j==ybound-1){
                    dir=3;
                    row--;
                    i--;
                    j++;
                }
            }
            else if(dir==3){
                ans[i--][j]=ind++;
                if(i==xbound-1 && j==ybound){
                    dir=0;
                    ybound++;
                    j++;
                    i++;
                }
            }
        }
        return ans;
    }
}