class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            # print(nums[:i], nums[i+1:])
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
            
        return -1