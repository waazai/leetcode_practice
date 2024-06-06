public class Solution {
    public bool IsNStraightHand(int[] hand, int groupSize) {

        // false when not divisiable
        if (hand.Length%groupSize!=0) return false;

        Array.Sort(hand);

        // the first card in the first group
        int i = 0;
        while(i<hand.Length){

            // skip used elements
            if (hand[i]==-1) i ++;
            else{
                int prev = hand[i];  // use to track if the next card is consecutive
                hand[i] = -1;  // mark this card used
                int j = i+1;
                int c = 1;  // count current group size

                while (c < groupSize){

                    if (j > hand.Length-1){
                        // if current group is not fulfilled
                        // and index reached the end
                        return false;
                    }
                    else if (hand[j]-prev==1){ // found consecutive card
                        prev = hand[j];
                        hand[j] = -1;
                        c ++;
                    }
                    j ++;
                }

                i ++;

                }

        }

        return true;
        
    }
}
