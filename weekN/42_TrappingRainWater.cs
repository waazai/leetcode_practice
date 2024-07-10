public class Solution {
    public int Trap(int[] height) {

        // record the highest left edge on each index
        int[] left_edge = new int[height.Length+1];
        int mx = height[0];
        for (int i=1; i<height.Length-1; i++){
            mx = Math.Max(mx, height[i-1]);
            left_edge[i] = mx;
        }
        // record the highest right edge on each index
        int[] right_edge = new int[height.Length+1];
        mx = height[height.Length-1];
        for (int i=height.Length-2; i>0; i--){
            mx = Math.Max(mx, height[i+1]);
            right_edge[i] = mx;
        }

        // sum the trapped water
        int water = 0;
        for (int i=1; i<height.Length-1; i++){
            water += Math.Max(0,Math.Min(left_edge[i], right_edge[i])-height[i]);
        }
        return water;
    }
