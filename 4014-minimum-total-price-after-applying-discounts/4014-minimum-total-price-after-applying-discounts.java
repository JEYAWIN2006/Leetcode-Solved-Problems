import java.util.Arrays;

class Solution {
    public double minPrice(int[] prices, int[] discounts) {
        Arrays.sort(prices);
        Arrays.sort(discounts);
        double sum = 0;
        int i = prices.length - 1;
        int j = discounts.length - 1;
        while (i >= 0 && j >= 0) {
            sum += prices[i] * (100 - discounts[j]) / 100.0;
            i--;
            j--;
        }
    
        while (i >= 0) {
            sum += prices[i];
            i--;
        }
        
        return sum;
    }
}
