class Solution(object):
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
        row = True
        forward = True
        while ((end_row - start_row) >= 0) and ((end_column - start_column) >= 0):
            if row:
                if forward:
                    for i in range(start_column, end_column+1):
                        spiral.append(matrix[start_row][i])
                    start_row += 1
                else:
                    for i in range(end_column, start_column-1, -1):
                        spiral.append(matrix[end_row][i])
                    end_row -= 1
                row = False
            else:
                if forward:
                    for i in range(start_row, end_row+1):
                        spiral.append(matrix[i][end_column])
                    end_column -= 1
                else:
                    for i in range(end_row, start_row-1, -1):
                        spiral.append(matrix[i][start_column])
                    start_column += 1
                row = True
                forward = not forward
        return spiral
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.spiralOrder(matrix))
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(matrix))

