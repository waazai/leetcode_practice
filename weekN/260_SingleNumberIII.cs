public class Solution {
    public int[] SingleNumber(int[] nums) {

        // let the answer [a, b]
        // we will get xor = a^b
        int xor = 0;
        foreach (int i in nums){
            xor ^= i;
        }

        // get a bit that a and b is different
        // -xor: invert all bits and add 1
        int setbit = xor & -xor;

        // group nums into 2
        // having setbit-th bit either 1 or 0
        // dulplicate num will always be grouped together
        // and canceled out when xoring
        // the 2 unique number will be seperate to the 2 group
        // and will remain after xoring
        int[] ans = [0,0];
        foreach (int i in nums){
            if ((setbit & i) == 0){
                ans[0] ^= i;
            }else{
                ans[1] ^= i;
            }
        }
        
        return ans;
    }
}
