public class Solution {
    public bool CanJump(int[] nums) {

        int idx = 0;
        int ap = 1;  // action pt 1 so that you can step on the first index
        int n = nums.Length;

        while (ap > 0){

            // use the remaining action points
            // or take the action points on idx
            // (decide wheter to jump to idx)
            ap = Math.Max(ap-1, nums[idx]);

            if (ap >= n-idx-1) return true;
            idx ++;
        }
        
        return false;
        
    }
}
