class Solution {
public:
    void bfs(int i,int j,vector <vector <int>> &visited,vector<vector<char>>& grid){
        visited[i][j]=1;
        queue <pair<int,int>> q;
        int n=grid.size();
        int m=grid[0].size();
        q.push({i,j});

        while(!q.empty()){
            int row=q.front().first;
            int col=q.front().second;
            q.pop();
            for(int delrow=-1;delrow<=1;delrow++){
                 
                    int nrow=row+delrow;
                  
                if(nrow>=0 && nrow<n && 
                 grid[nrow][col]=='1' && !visited[nrow][col] ){
                    visited[nrow][col]=1;
                    q.push({nrow,col});
                }
            
            }
           
            for(int delcol=-1;delcol<=1;delcol++){
                int ncol=col+delcol;
                if( ncol>=0 && ncol<m &&
                 grid[row][ncol]=='1' && !visited[row][ncol] ){
                    visited[row][ncol]=1;
                    q.push({row,ncol});
                }
            }
            }
        }
    
    int numIslands(vector<vector<char>>& grid) {
        int n=grid.size();
        int m=grid[0].size();
        int count=0;
        vector <vector <int>> visited(n,vector<int>(m,0));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]=='1' && !visited[i][j]){
                count++;
                bfs(i,j,visited,grid);
                
                }
            }
        }
        return count;
    }
};