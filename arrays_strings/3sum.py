'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

Two Sum uses a hashmap to find complement values, and therefore achieves \mathcal{O}(N)O(N) time complexity.
Two Sum II uses the two pointers pattern and also has \mathcal{O}(N)O(N) time complexity for a sorted array.
We can use this approach for any array if we sort it first, which bumps the time complexity to \mathcal{O}(n\log{n})O(nlogn).
'''
'''
#Approach 1: Two Pointers
Complexity Analysis

Time Complexity: \mathcal{O}(n^2)O(n2). twoSumII is \mathcal{O}(n)O(n), and we call it nn times.
Sorting the array takes \mathcal{O}(n\log{n})O(nlogn), so overall complexity is \mathcal{O}(n\log{n} + n^2)O(nlogn+n). 
This is asymptotically equivalent to \mathcal{O}(n^2)O(n2).

Space Complexity: from \mathcal{O}(\log{n})O(logn) to \mathcal{O}(n)O(n), depending on the implementation of the sorting algorithm. For the purpose of complexity analysis, we ignore the memory required for the output.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                  
'''                  
#Approach 2: HashSet

Time Complexity: \mathcal{O}(n^2)O(n2). twoSum is \mathcal{O}(n)O(n), and we call it nn times.
Sorting the array takes \mathcal{O}(n\log{n})O(nlogn), so overall complexity is \mathcal{O}(n\log{n} + n^2)O(nlogn+n2). 
This is asymptotically equivalent to \mathcal{O}(n^2)O(n2).

Space Complexity: \mathcal{O}(n)O(n) for the hashset.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
            
 '''
Approach 3: "No-Sort"
Time Complexity: \mathcal{O}(n^2)O(n2). We have outer and inner loops, each going through nn elements.While the asymptotic complexity is the same, 
this algorithm is noticeably slower than the previous approach. Lookups in a hashset, though requiring a constant time, are expensive compared to the direct memory access.

Space Complexity: \mathcal{O}(n)O(n) for the hashset/hashmap.For the purpose of complexity analysis, we ignore the memory required for the output.
However, in this approach we also store output in the hashset for deduplication. In the worst case, there could be 
\mathcal{O}(n^2)O(n2) triplets in the output, like for this example: [-k, -k + 1, ..., -1, 0, 1, ... k - 1, k]. 
Adding a new number to this sequence will produce n / 3 new triplets.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res

