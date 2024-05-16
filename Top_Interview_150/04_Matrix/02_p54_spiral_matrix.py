class Solution(object):
    # Runtime = 12ms, beats 73.18%. Memory = 11.66 MB, beats 43.59%
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        start_row = 0
        end_row = len(matrix)-1
        start_column = 0
        end_column = len(matrix[0])-1
        row = True # Looking at row or column
        forward = True
        # Loops until we have visited all indices
        while ((end_row - start_row) >= 0) and ((end_column - start_column) >= 0):
            if row:
                # Add values in topmost remaining row from left to right
                if forward:
                    for i in range(start_column, end_column+1):
                        spiral.append(matrix[start_row][i])
                    start_row += 1 # Have visited all indices in top row
                # Add values in bottom-most remaining row from right to left
                else:
                    for i in range(end_column, start_column-1, -1):
                        spiral.append(matrix[end_row][i])
                    end_row -= 1 # Have visited all indices in bottom row
                row = False # Look at column next iteration
            else:
                # Add values in rightmost remaining column from top to bottom
                if forward:
                    for i in range(start_row, end_row+1):
                        spiral.append(matrix[i][end_column])
                    end_column -= 1
                # Add values in leftmost remaining column from bottom to top
                else:
                    for i in range(end_row, start_row-1, -1):
                        spiral.append(matrix[i][start_column])
                    start_column += 1
                row = True # Look at row next iteration
                forward = not forward # Reverse direction next row
        return spiral
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.spiralOrder(matrix))
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(matrix))

