class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        left = start = 0
        mem = {}
        res = 0
        for right in range(len(nums)):
            x = nums[right]
            if x in mem:
                mem[x] += 1
            else:
                mem[x] = 1
                
            if len(mem) == k + 1:
                del mem[nums[left]]
                left += 1
                start = left
                
        
            if len(mem) == k:
                while mem[nums[left]] > 1:
                    mem[nums[left]] -= 1
                    left += 1
                
                res += left - start + 1
        return res
            