public class Solution {
    public int HIndex(int[] citations) {

        int n = citations.Length;

        // idx = cited times
        // value = # of research cited this much time
        // n represent any research that is cited more than n times
        int[] freq = new int[n+1];
        for (int i=0; i<n; i++){
            if (citations[i]>n) freq[n] +=1;
            else freq[citations[i]] +=1;
        }

        // starting from the end
        // keep track of the # of research cited
        // return when that # is greater than cited times (idex of freq)
        int c = 0;
        for (int i=n; i>-1; i--){
            c += freq[i];
            if (c>=i) return i;
        }
        return -1;
    }
}
