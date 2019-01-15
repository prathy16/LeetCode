# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution {
public:
    bool hasAlternatingBits(int n) {
        int b = n & 1;
        
        while((n&1) == b)
        {
            b = 1 - b;
            n = n >> 1;
        }
        
        return n==0;
    }
};
