'''

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.
             
'''

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        rowsum, colsum = [0] * n, [0] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rowsum[i] += 1
                    colsum[j] += 1
        k = sum(rowsum)
        
        rowcost, colcost = [0] * n, [0] * m
        rowcost[0] = sum([i*r for i,r in enumerate(rowsum)])
        behind = rowsum[0]
        for i in range(1, n):
            rowcost[i] = rowcost[i-1] + behind - (k - behind)
            behind += rowsum[i]
            
        colcost[0] = sum([j*c for j,c in enumerate(colsum)])
        behind = colsum[0]
        for j in range(1, m):
            colcost[j] = colcost[j-1] + behind - (k - behind)
            behind += colsum[j]
        
        return min(rowcost) + min(colcost)
        
