'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            self.empty = True
            return
        else:
            self.empty = False
            
        row = len(matrix)
        col = len(matrix[0])
        self.matrix = matrix
        self.summatrix = [[0] * (col+1) for i in range(row)]

        for i in range(row):
            for j in range(1, col+1):
                self.summatrix[i][j] = matrix[i][j-1] + self.summatrix[i][j-1]
        
    def update(self, row: int, col: int, val: int) -> None:
      
        if self.empty:
            return
        
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        col += 1
        ncol = len(self.summatrix[0])
        
        for i in range(col, ncol):
            self.summatrix[row][i] = self.summatrix[row][i] + diff
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.empty:
            return 0
        
        col1, col2 = col1+1, col2+1
        ans = 0
        for row in range(row1, row2+1):
            ans += self.summatrix[row][col2] - self.summatrix[row][col1-1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
