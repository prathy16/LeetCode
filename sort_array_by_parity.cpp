// Problem: https://leetcode.com/problems/sort-array-by-parity/

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int i, j;
        i = 0, j = 0;
        
        while(j < A.size() && i < A.size())
        {
            if(i != j)
            {
                if(A[i]%2 == 1 && A[j]%2 == 0)
                {
                    int temp;
                    temp = A[i];
                    A[i] = A[j];
                    A[j] = temp;
                    i++;
                    j++;
                }
                else if(A[i]%2 == 1 && A[j]%2 == 1)
                    j++;
                else
                    i++;
            }
            else
                j++;
        }
        
        return A;
    }
};
