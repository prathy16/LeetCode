# https://leetcode.com/problems/unique-email-addresses/

class Solution {
public:
    string f(string email)
    {
        int pos = email.find('@');
        string local = email.substr(0, pos);
        string domain = email.substr(pos+1);
        
        string tmp = "";
        for(char c: local)
        {
            if(c == '+') break;
            if(c != '.') tmp += c;
        }
        
        return tmp + '@' + domain;
    }
    int numUniqueEmails(vector<string>& emails) {
        set<string> unique_emails;
        for(auto& email: emails)
        {
            unique_emails.insert(f(email));
        }
        
        return unique_emails.size();
    }
};
