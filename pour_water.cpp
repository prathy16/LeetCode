# https://leetcode.com/problems/pour-water/

class Solution {
public:
    vector<int> pourWater(vector<int>& heights, int V, int K) {
        int i, n = heights.size();
        while(V--)
        {
            i = K;
            for(int j = K-1; j >= 0; j--)
            {
                if(heights[j] > heights[i]) break;
                else if(heights[j] < heights[i]) i = j;
            }
            
            if(i == K)
            {
                for(int j = K+1; j<n; j++)
                {
                    if(heights[j] > heights[i]) break;
                    else if(heights[j] < heights[i]) i = j;
                }
            }
            
            heights[i] += 1;
        }
        
        return heights;
    }
};

