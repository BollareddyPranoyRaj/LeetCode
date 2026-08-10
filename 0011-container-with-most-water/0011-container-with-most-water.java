class Solution {
    public int maxArea(int[] height) {
        int n=height.length;
        int max=Integer.MIN_VALUE;
        int i=0;int j=n-1;int num=0;
        while(i<j){
            num=(j-i)*Math.min(height[i],height[j]);
            max=Math.max(max,num);
            if(height[i]<height[j]){
                i++;
            }
            else{
                j--;
            }
        }
        return max;
    }
}