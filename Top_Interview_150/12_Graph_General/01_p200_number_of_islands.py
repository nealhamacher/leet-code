class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # Set to store visited cells
        visited = set()

        #Initialize number of islands
        num_islands = 0

        # Helper function - finds the cells part of a continous island
        def findIsland(i, j):
            # Off the map - end recursion
            if i<0 or i>= len(grid) or j<0 or j>=len(grid[0]):
                return 0
            # Already visited
            if (i,j) in visited:
                return 0
            # Water cell - not part of an island
            if grid[i][j] == '0':
                visited.add((i,j))
                return 0
            
            # Recursive case - find all land cells connected to current island
            #   add these to visited, return 1 for the island
            visited.add((i,j))
            findIsland(i+1, j)
            findIsland(i, j+1)
            return 1


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                num_islands += findIsland(i,j)

        return num_islands
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
    print(sol.numIslands(grid))
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    print(sol.numIslands(grid))