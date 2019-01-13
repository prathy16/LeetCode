# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution {
public:
    int minAddToMakeValid(string S) {
        stack<char> stackPar;
        int count = 0;
        
        for(char c: S)
        {
            if(c == '(')
                stackPar.push(c);
            else if(!stackPar.empty())
                stackPar.pop();
            else
                count++;
        }
        
        while(!stackPar.empty())
        {
            count += 1;
            stackPar.pop();
        }
        
        return count;
    }
};
