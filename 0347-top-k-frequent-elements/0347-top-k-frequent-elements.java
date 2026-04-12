import java.util.*;
class Solution{
    public int[] topKFrequent(int[] nums,int k){
        Arrays.sort(nums);
        int n=nums.length;
        int[] values=new int[n];
        int[] freq=new int[n];
        int index=0;
        int count=1;
        for(int i=1;i<n;i++){
            if(nums[i]==nums[i-1]){
                count++;
            }else{
                values[index]=nums[i-1];
                freq[index]=count;
                index++;
                count=1;
            }
        }
        values[index]=nums[n-1];
        freq[index]=count;
        index++;
        for(int i=0;i<index;i++){
            for(int j=i+1;j<index;j++){
                if(freq[j]>freq[i]){
                    int temp=freq[i];
                    freq[i]=freq[j];
                    freq[j]=temp;
                    temp=values[i];
                    values[i]=values[j];
                    values[j]=temp;
                }
            }
        }
        int[] arr=new int[k];
        for(int i=0;i<k;i++){
            arr[i]=values[i];
        }
        return arr;
    }
}