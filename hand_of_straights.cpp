# https://leetcode.com/problems/hand-of-straights/

class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        map<int, int> counts;
        for(int num: hand) counts[num]++;
        
        for(auto it: counts)
        {
            if(counts[it.first] > 0)
            {
                for(int i = W-1; i>=0; i--)
                    if((counts[it.first+i] -= counts[it.first]) < 0)
                        return false;
            }
        }
        
        return true;
    }
};
