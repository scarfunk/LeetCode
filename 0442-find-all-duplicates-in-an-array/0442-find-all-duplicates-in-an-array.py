import collections

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        # print(cnt)
        
        return list([k for k, v in cnt.items() if v > 1])
        