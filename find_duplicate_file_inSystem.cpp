# https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        unordered_map<string, vector<string>> hashtable;
        vector<vector<string>> filePaths;
        for(string path: paths)
        {
            stringstream ss(path);
            string root, word;
            getline(ss, root, ' ');
            
            while(getline(ss, word, ' '))
            {
                int start = word.find('(');
                string fileName = root + "/" + word.substr(0, start);
                string fileContent = word.substr(start+1, word.size()-start-2);
                
                hashtable[fileContent].push_back(fileName);
            }
        }
        
        for(auto it: hashtable)
        {
            if(it.second.size() > 1)
                filePaths.push_back(it.second);
        }
        return filePaths;
    }
};
