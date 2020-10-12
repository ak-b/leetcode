'''
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.
You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.
Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.
Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]

Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.

Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]

'''
def is_possible(sweetness: List[int], target: int, n: int) -> bool:
    """ 
    Is it possible to split up sweetness array into n parts,
    such that each part has atleast target sweetness
    """
    left = -1
    current = 0
    for right in range(len(sweetness)):
        s = sweetness[right]
        current += s
        if current >= target:
            n -= 1
            left = right
            current = 0
            if n == 0:
                return True
    return False


def maximize_sweetness(sweetness: List[int], K: int):
    total = sum(sweetness)  # total sweetness
    lo = 0
    hi = total // (K+1)     # maximum sweetness that can be achieved
    result = 0
    
    # now we will just do a binary search between the lo and hi value
    while lo <= hi:
        mid = (lo + hi) // 2
        if is_possible(sweetness, mid, K+1):
            result = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return result
    


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        return maximize_sweetness(sweetness, K)
