'''
Given a list of query words, return the number of words that are stretchy. 
'''
import itertools
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        group = lambda x: [(k, len(list(v))) for k, v in itertools.groupby(x)]
        S, count = group(s), 0
        for W in map(group, words):
            if len(W) != len(S): continue
            for s, w in zip(S, W):
                if s[0] != w[0] or s[1] < w[1] or w[1] < s[1] < 3:
                    break
            else:
                count += 1
        return count
