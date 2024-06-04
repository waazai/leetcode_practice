public class Solution {
    public int Jump(int[] nums) {

        int n = nums.Length;
        int idx = 0;
        int step = 0;
        int jump_point = 0;  // previous jump
        int jump = 0;

        while (jump_point < n-1){

            // upadate reachable step
            step = Math.Max(step, idx+nums[idx]);

            // when loop to the jump point
            // update jump point and confirm the jump
            if (idx == jump_point){
                jump_point = step;
                jump ++;
            }
            
            idx ++;
        }

        return jump;

    }
}
