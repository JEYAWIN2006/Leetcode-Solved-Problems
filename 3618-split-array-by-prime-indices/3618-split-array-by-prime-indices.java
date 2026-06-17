class Solution { 
    public static boolean isPrime(int n) { 
        if (n <= 1) { return false; } 
        if (n == 2) { return true; } 
        if (n % 2 == 0) { return false; } 
        for (int i = 3; i * i <= n; i += 2) { 
            if (n % i == 0) { return false; } 
        } 
        return true; 
    } 

    public long splitArray(int[] nums) { 
        long sum = 0; 
        long sum2 = 0; 

        for (int i = 0; i < nums.length; i++) { 
            if (isPrime(i)) { 
                sum += nums[i]; 
            } else { 
                sum2 += nums[i]; 
            } 
        } 
        return Math.abs(sum - sum2); 
    } 
}
