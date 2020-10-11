class Solution(object):
    def isStrobogrammatic(self, num):
        barriercase = [('6','9'),('9','6')]
        standardcase = ['1', '8', '0']
        invalidcase = {'2': 0, '3': 0, '4': 0, '5': 0, '7': 0}
        
        start = 0
        mid = (len(num)//2) -1
        
        while start <= mid:
            if num[start] not in standardcase or num[len(num)-1-start] != num[start]:
                if (num[start], num[len(num)-1-start]) not in barriercase:
                    return False
            start += 1
        if len(num)%2 != 0:
            if num[len(num)//2] not in standardcase:
                return False
        return True
