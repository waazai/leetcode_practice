public class Solution {
    public int RemoveDuplicates(int[] nums) {

        // the index to compare if there is duplicate
        int ptr = 0;
        for (int i=ptr+1; i<nums.Length; i++){

            // when encounter a different val
            if (nums[i]!=nums[ptr]){

                // place the different val to the next index
                nums[ptr+1]=nums[i];
                // update the index to compare
                ptr ++;
            }
        }
        // return the length == index +1
        return ptr + 1;
    }
}
