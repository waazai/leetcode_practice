public class Solution {
    public int RemoveDuplicates(int[] nums) {

        // array with length 1 ot 2 do not need to modify
        if (nums.Length<3) return nums.Length;

        // the index to check
        int k = 1;

        for (int i=k+1; i<nums.Length; i++){
            
            // when k is different to the new encount
            // or k-1 is different to k
            // place the new encount next to k
            // this 3 elements matches the condition
            // so move pointer k to the end of these 3 elements
            if (nums[i]!=nums[k] | nums[k]!=nums[k-1]){
                nums[k+1] = nums[i];
                k ++;
            }
        }

        // return length, so index+1
        return k + 1;
    }
}
