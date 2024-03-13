class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i,v in enumerate(nums):
            mem[v] = i
        print(mem)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mem and i != mem[diff]:
                return [i, mem[diff]]
