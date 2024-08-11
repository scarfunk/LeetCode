class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mem = {}
        for n in nums:
            mem[n] = n
        
        print(mem)
        ret = []
        for i in range(1, len(nums)+1):
            if i not in mem:
                ret.append(i)
                
        return ret