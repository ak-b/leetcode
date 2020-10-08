'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]

Solution:
Approach 1 : Transpose and then reverse
The obvious idea would be to transpose the matrix first and then reverse each row. This simple approach already demonstrates the best possible time complexity \mathcal{O}(N^2)O(N2).

Approach 2 : Rotate four rectangles
Intuition
Approach 1 makes two passes through the matrix, though it's possible to make a rotation in one pass.

Approach 3 : Rotate four rectangles in one single loop
The idea is the same as in the approach 2, but everything is done in one single loop and hence it's a way more elegant (kudos go to @gxldragon).

for all three approaches 
Time complexity : O(N^2)is a complexity given by two inserted loops.
Space complexity : O(1) since we do a rotation in place.
'''
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])        
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
