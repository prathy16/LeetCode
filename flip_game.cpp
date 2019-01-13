# https://leetcode.com/problems/flip-game/

class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        vector<string> flips;
        
        for(int i = 1; i < s.size(); i++)
        {
            if(s.substr(i-1, 2) == "++")
            {
                string s1 = s.substr(0, i-1);
                if(i+1 < s.size())
                {
                    string s2 = s.substr(i+1, s.size()-i-1);
                    flips.push_back(s1+"--"+s2);
                }
                else
                    flips.push_back(s1+"--");
            }
        }
        
        return flips;
    }
};
