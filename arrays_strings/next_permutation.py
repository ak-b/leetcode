'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:

Input: nums = [1]
Output: [1]
'''
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #>right
        i = len(nums)-1
        while i-1>=0 and nums[i-1]>=nums[i]:
            i -=1
        #>left
        if i-1>=0:
            j = i
            while j<len(nums) and nums[j]>nums[i-1]:
                j +=1
            #swap the min-max number
            nums[i-1],nums[j-1] = nums[j-1],nums[i-1]
        m = i
        n = len(nums)-1
        while m < n:
            nums[m],nums[n] = nums[n],nums[m]
            m +=1
            n -=1
