'''
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"

Example 2:

Input: nums = [], lower = 1, upper = 1
Output: ["1"]
Explanation: The only missing range is [1,1], which becomes "1".

Example 3:

Input: nums = [], lower = -3, upper = -1
Output: ["-3->-1"]
Explanation: The only missing range is [-3,-1], which becomes "-3->-1".

Example 4:

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.

Example 5:

Input: nums = [-1], lower = -2, upper = -1
Output: ["-2"]
'''

#Approach 1: Linear Scan
'''
Intuition and Algorithm
Since the input array, nums, is sorted ascendingly and all the elements in it are within the given [lower, upper] bounds, 
we can simply check consecutive elements to see if they differ by one or not. If they don't, then we have found a missing range.

When nums[i] - nums[i-1] == 1, we know that there are no missing elements between nums[i-1] and nums[i].
When nums[i] - nums[i-1] > 1, we know that [nums[i-1] + 1, nums[i] - 1] range of elements are missing.
'''

# Time:  O(n)
# Space: O(1)
#
# Given a sorted integer array where the range of elements are [lower, upper] inclusive,
# return its missing ranges.
# 
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, 
# return ["2", "4->49", "51->74", "76->99"].
#

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []

        def add(low, high):
            if low > high:
                return
            if low == high:
                result.append(str(low))
            else:
                result.append(str(low) + '->' + str(high))

        if not nums: # edge case
            add(lower, upper)
            return result

        add(lower, nums[0] - 1)

        for x in range(len(nums)):
            add(nums[x - 1] + 1, nums[x] - 1)

        add(nums[-1] + 1, upper)

        return result
