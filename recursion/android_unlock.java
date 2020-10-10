'''
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:

-Each pattern must connect at least m keys and at most n keys.
-All the keys must be distinct.
-If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
-The order of keys used matters.

'''

#Bakctracking
'''
Algorithm

The algorithm uses backtracking technique to enumerate all possible kk combinations of numbers [1\dots 9][1…9] where m \leq k \leq nm≤k≤n. 
During the generation of the recursive solution tree, the algorithm cuts all the branches which lead to patterns which doesn't satisfy 
the rules and counts only the valid patterns. In order to compute a valid pattern, the algorithm performs the following steps:
Select a digit ii which is not used in the pattern till this moment. This is done with the help of a usedused array which stores all available digits.
We need to keep last inserted digit lastlast. The algorithm makes a check whether one of the following conditions is valid.
There is a knight move (as in chess) from lastlast towards ii or lastlast and ii are adjacent digits in a row, in a column. 
In this case the sum of both digits should be an odd number.
The middle element midmid in the line which connects ii and lastlast was previously selected. In case ii and lastlast are positioned 
at both ends of the diagonal, digit midmid = 5 should be previously selected.lastlast and ii are adjacent digits in a diagonal
In case one of the conditions above is satisfied, digit ii becomes part of partially generated valid pattern and the algorithm continues 
with the next candidate digit till the pattern is fully generated. Then it counts it. In case none of the conditions are satisfied,
the algorithm rejects the current digit ii, backtracks and continues to search for other valid digits among the unused ones.
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
