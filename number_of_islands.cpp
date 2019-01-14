# https://leetcode.com/problems/number-of-islands/

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        if(n == 0) return 0;
        int m = grid[0].size();
        int count = 0;
        
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if(grid[i][j] == '1')
                {
                    count++;
                    updateGrid(grid, i, j, n, m);
                }
            }
        }
        return count;
    }
    
private:
    void updateGrid(vector<vector<char>>& grid, int i, int j, int n, int m){
        grid[i][j] = '0';
        if(i+1<n && grid[i+1][j] == '1')
            updateGrid(grid, i+1, j, n, m);
        if(j+1<m && grid[i][j+1] == '1')
            updateGrid(grid, i, j+1, n, m);
        if(i-1>=0 && grid[i-1][j] == '1')
            updateGrid(grid, i-1, j, n, m);
        if(j-1>=0 && grid[i][j-1] == '1')
            updateGrid(grid, i, j-1, n, m);
    }
};
