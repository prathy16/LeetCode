# https://leetcode.com/problems/perfect-squares/

class Solution {
public:
    int numSquares(int n) {
        vector<int> perfectSquares(n+1, INT_MAX);
        
        if(n<=0) {
            return 0;
        }
        
        perfectSquares[0] = 0;
        for(int i = 1; i < n+1; i++)
        {
            for(int j = 1; j*j <= i; j++)
            {
                perfectSquares[i] = min(perfectSquares[i], perfectSquares[i-j*j]+1);
            }
        }
        
        return perfectSquares[n];
    }
};
