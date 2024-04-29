class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 110
        # 001
        # 010
        # 100
        
        # 010
        # 001
        # 011
        # 100
        
        # 100 001
        
        ret = 0
        for n in nums:
            ret = ret ^ n
            
        res = bin(ret ^ k)[2:].count("1")
        print(res)
        return res