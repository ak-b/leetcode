'''
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].
'''
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""

        numStack = []
        charStack = []
        res = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                count = 0
                while s[i].isdigit():
                    count = count * 10 + int(s[i])
                    i = i+1
                numStack.append(count)
            elif s[i] == '[':
                charStack.append(res)
                res = ''
                i=i+1
            elif s[i] == ']':
                temp = charStack.pop()
                c = int(numStack.pop())
                j = 0
                while j < c:
                    temp+=res
                    j=j+1
                res = temp
                i+=1
            else:
                res+=(s[i])
                i = i +1
        return res
