# https://leetcode.com/problems/array-partition-i/

class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        vector<int> hashtable(20001, 0);
        
        for(int n: nums) 
            hashtable[n+10000]++;
        
        bool flag = true;
        int min_sum = 0;
        
        int i = 0;
        
        while(i < 20001)
        {
            if(hashtable[i] >= 1)
            {
                min_sum = flag ? min_sum+i-10000 : min_sum;
                flag = flag ^ 1;
                hashtable[i]--;
            }
            else i++;
        }
        
        return min_sum;
    }
};
