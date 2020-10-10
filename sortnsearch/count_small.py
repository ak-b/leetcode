'''
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

lass Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        d = {}
        newnums = []
        for i in range(len(nums)):
            newnums.append((i, nums[i]))
        count = [0] * len(newnums)
        return self.helper(newnums, count)[1]
    
    def helper(self, nums: List[int], count: List[int]) -> (List[int], List[int]):
        if nums == []:
            return ([], count)
        elif len(nums) == 1:
            return ([nums[0]], count)
        mid = int(len(nums)/2)
        left = self.helper(nums[:mid], count)
        right = self.helper(nums[mid:], count)
        return self.mergeCount(left[0], right[0], count)
    
    def mergeCount(self, numsLeft: List[int], numsRight: List[int], count: List[int]) -> (List[int], List[int]):
        numsSorted = []
        i = 0
        j = 0
        addition = len(numsRight)
        
        while i < len(numsLeft) and j < len(numsRight):
            if numsLeft[i][1] > numsRight[j][1]:
                count[numsLeft[i][0]] += addition
                numsSorted.append(numsLeft[i])
                i += 1
            else:
                numsSorted.append(numsRight[j])
                addition -= 1
                j += 1
        
        if i == len(numsLeft):
            while j < len(numsRight):
                numsSorted.append(numsRight[j])
                j += 1           
        
        elif j == len(numsRight):
            while i < len(numsLeft):
                numsSorted.append(numsLeft[i])
                i += 1
                
        return (numsSorted, count)
