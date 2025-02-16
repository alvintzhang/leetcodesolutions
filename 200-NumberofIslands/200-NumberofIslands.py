class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # Build helper to pop all 1s from an island
        # Add to count

        def findIsland(self, grid,x,y):
            if(y<0 or x<0 or y>=len(grid[0]) or x>=len(grid)): 
                return None
            if(grid[x][y]=='1'):
                print(grid[x][y])
                grid[x][y] = '0'
                findIsland(self,grid,x,y+1)
                findIsland(self,grid,x+1,y)
                findIsland(self,grid,x,y-1)
                findIsland(self,grid,x-1,y)
            else:
                return None
        
        total = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if(grid[x][y]=='1'):
                    total+=1
                    findIsland(self, grid, x,y)

        return total