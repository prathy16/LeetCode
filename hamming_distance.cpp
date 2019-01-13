# https://leetcode.com/problems/hamming-distance/

class Solution {
public:
    int hammingDistance(int x, int y) {
        int dist = 0, diff = x^y;
        
        while(diff)
        {
            ++dist;
            diff = diff & (diff-1);
        }
        
        return dist;
    }
};
