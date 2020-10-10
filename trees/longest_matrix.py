'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
'''
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        NOTVISITED = -1
        VISITING = -2
        NOPREV = -3
        mark = [[NOTVISITED for _ in matrix[0]] for _ in matrix]
        dirs = ((1,0), (-1,0), (0,1), (0,-1))
        def dfs(i, j, prev):
            if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or mark[i][j] == VISITING:
                return 0
            if prev != NOPREV and matrix[i][j] <= prev:
                return 0
            if mark[i][j] != NOTVISITED:
                return mark[i][j]
            mark[i][j] = VISITING
            leng = 0
            for di, dj in dirs:
                leng = max(leng, 1+dfs(i+di, j+dj, matrix[i][j]))
            mark[i][j] = leng
            return leng
        
        leng = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                leng = max(leng, dfs(i, j, NOPREV))
        return leng
