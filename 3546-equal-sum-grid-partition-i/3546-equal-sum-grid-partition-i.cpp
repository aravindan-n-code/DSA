class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();

    long long totalSum = 0;
    for(auto &row : grid)
        for(int val : row)
            totalSum += val;

    // Vertical cut
    long long prefix = 0;
    for(int j = 0; j < cols - 1; j++) {
        for(int i = 0; i < rows; i++) {
            prefix += grid[i][j];
        }
        if(prefix == totalSum - prefix)
            return true;
    }

    // Horizontal cut
    prefix = 0;
    for(int i = 0; i < rows - 1; i++) {
        for(int j = 0; j < cols; j++) {
            prefix += grid[i][j];
        }
        if(prefix == totalSum - prefix)
            return true;
    }

    return false;
}
};