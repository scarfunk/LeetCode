from itertools import combinations, permutations

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        combi = list(combinations(arr, 2))
        combi.sort(key = lambda x : (x[0]/x[1]))
        # print(combi)
        return combi[k-1]