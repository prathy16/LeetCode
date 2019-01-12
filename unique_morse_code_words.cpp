# https://leetcode.com/problems/unique-morse-code-words/

class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        unordered_map<string, int> code;
        vector<string> morsecodes = {".-","-...","-.-.","-..",".","..-.",
                                     "--.","....","..",".---","-.-",".-..",
                                     "--","-.","---",".--.","--.-",".-.","...",
                                     "-","..-","...-",".--","-..-","-.--","--.."};
        for(string s: words)
        {
           string tmp = "";
           for(char c: s)
               tmp += morsecodes[c-97];
            code[tmp]++;
        }
        
        return code.size();
    }
};
