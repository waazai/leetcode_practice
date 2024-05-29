public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {

        // do not need nums2, return
        if (n == 0) return;

        // sorting from the end
        int ptr = m+n-1;

        while (m>0 && n>0){

            // append the larger element to the end
            if (nums1[m-1] >= nums2[n-1]){
                nums1[ptr] = nums1[m-1];
                m --;
            }else{
                nums1[ptr] = nums2[n-1];
                n --;
            }
            ptr --;
        }

        // append if nums2 remained
        while (n > 0){
            nums1[ptr] = nums2[n-1];
            n --;
            ptr --;
        }
    }
}
