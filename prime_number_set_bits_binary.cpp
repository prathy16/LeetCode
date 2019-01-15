# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution {
public:
    int countPrimeSetBits(int L, int R) {
        set<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        int count = 0;
        
        for(int i=L; i<=R; i++)
        {
            int bits = 0;
            for(int j = i; j; j >>= 1)
                bits = bits + (j & 1);
            
            count += primes.count(bits);
        }
    
        return count;
    }
};
