'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, 
such that the container contains the most water.

Notice that you may not slant the container.
'''
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n=len(height)
        if n == 2:
            return min(height[0],height[1])
        else:
            l=0
            r=n-1
            clh=0
            crh=0
            maxa=0 
            while l<r :                
              
                if height[l]<height[r]:
                    maxa=max(height[l]*(r-l),maxa)
                    clh=height[l]
                    while height[l]<=clh:
                        l+=1
                        if l>= r:
                            return maxa

                else:
                    maxa=max(height[r]*(r-l),maxa)
                    crh=height[r]
                    while height[r]<=crh :
                        r-=1 
                        if l>= r:
                            return maxa
                        

            return maxa
