'''
On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
'''
class Solution(object):
    def minmaxGasDist(self, stations, K):
        def possible(D):
            return sum(int((stations[i+1] - stations[i]) / D)
                       for i in range(len(stations) - 1)) <= K

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo
