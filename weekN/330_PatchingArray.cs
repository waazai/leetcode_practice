public class Solution {
    public int MinPatches(int[] nums, int n) {

        // greedy
        
        int range = 0;  // the range that is already patched
        int patch = 0;  // # of patch

        for (int i=0; i<nums.Length; i++){
            if (range>=n) return patch;

            // if there is a gap that need patch
            while (nums[i]-range >=2){ 
                // patch the number that is 1 greater than the range
                range += range+1; 
                patch ++; 
                if (range>=n) return patch;
            }

            range += nums[i];
        }

        // when need to patch after iterated nums
        while (range<n){
            patch ++;
            // deal with large num that int cannot hold
            if (range-1 >= int.MaxValue/2) return patch;
            range += range+1;
        }

        return patch;
    }
}
