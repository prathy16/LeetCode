#
class Solution {
public:
    string toLowerCase(string str) {
        for(char &c: str)
        {
            if(c>='A' && c<='Z') 
              c = c + 32;
            // c = tolower(c);
        }
        
        return str;
    }
};
