public class Solution {
    public int CountTriplets(int[] arr) {

        // prefix array to store the xor result
        // prfx[i] = arr[0]^...^arr[i-1]
        // arr[l]^...^arr[r] = prfx[r+1]^prfx[l]
        int[] prfx = new int[arr.Length+1];
        for (int i=0; i<arr.Length; i++){
            prfx[i+1] = prfx[i]^arr[i];
        }

        // a==b if a^b==0
        // so arr[i]^...^arr[k] should be 0
        // => prfx[k+1]^prfx[i] == 0
        // => find all prfx[i]==prfx[k+1]
        int c = 0;
        for (int i=0; i<arr.Length; i++){
            for (int k = i+1; k<arr.Length; k++){
                if (prfx[i] == prfx[k+1]){
                    // And all j within i<j<=k can satisfy the condition a==b
                    c += (k-i);
                }
            }
        }
        
        return c;
    }
}
