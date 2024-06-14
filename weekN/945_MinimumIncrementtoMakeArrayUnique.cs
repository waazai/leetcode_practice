public class Solution {
    public int MinIncrementForUnique(int[] nums) {

        // create a frequency dict
        // record the max number for as iteration range
        var dict = new Dictionary<int, int>();
        int mx_rng = nums.Length;
        foreach (int i in nums){
            if (!dict.ContainsKey(i)) dict.Add(i, 1);
            else dict[i] ++;
            mx_rng = Math.Max(i, mx_rng+1);
        }

        // when loop to a number with frequency greater than 1
        // add the exceeding frequnecy to the next number
        // update count
        int c = 0;
        for (int i=0; i<mx_rng; i++){
            if (!dict.ContainsKey(i)) continue;
            if (dict[i]<=0) continue;
            int freq = dict[i]-1;
            c += freq;
            if (!dict.ContainsKey(i+1)) dict.Add(i+1, freq);
            else dict[i+1] += freq; 
        }
        return c;
    }
}
