# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word, reversedstring = "";
        
        while(ss >> word)
        {
            reverse(word);
            reversedstring += word + " ";
        }
        
        return reversedstring.substr(0, reversedstring.size()-1);
    }
    
private:
    void reverse(string& word)
    {
        int i, j;
        i = 0, j = word.size()-1;
        
        while(i < j) 
        {
            swap(word[i++], word[j--]);
        }
    }
};
