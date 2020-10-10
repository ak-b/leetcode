'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
'''
class Solution:
    
    def recursive(self, n, N):
        if n == 0:
            return [""]
        elif n == 1:
            return ["0", "1", "8"]
        
        inner = self.recursive(n - 2, N)
        comb = [["6", "9"], ["9", "6"], ["1", "1"], ["8", "8"], ["0", "0"]]
        
        ans = []
        for v in inner:
            for c in comb:
                res = c[0] + v + c[1]
                if n == N and str(int(res)) != res:
                    continue
                ans.append(res)
        return ans
    
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        return self.recursive(n, n)
