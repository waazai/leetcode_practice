public class Solution {
    public int NumSteps(string s) {

        int n  = s.Length;
        int nxt = 0;
        int cur = 0;
        int c = 0;

        for (int i=n-1; i>0; i--){
            
            // =1 if odd, =0 if even
            cur = s[i]-'0';

            // if even, cost a step to reduce the 1 string length
            // if odd, cost a step to change end bit to 1
            c ++;

            // if even, no extra step here
            // if odd, string length will change if need to carry on
            // add extra step for it
            c += cur^nxt;
            nxt = cur|nxt;
        }

        // end case
        return c+nxt;
    }
}
