# https://leetcode.com/problems/robot-return-to-origin/

class Solution {
public:
    bool judgeCircle(string moves) {
        pair<int, int> move = {0, 0};
        
        for(char c: moves)
        {
            if(c == 'L')
                move = {move.first-1, move.second};
            if(c == 'R')
                move = {move.first+1, move.second};
            if(c == 'U')
                move = {move.first, move.second+1};
            if(c == 'D')
                move = {move.first, move.second-1};
        }
        
        if(move.first == 0 && move.second == 0) return true;
        return false;
    }
};
