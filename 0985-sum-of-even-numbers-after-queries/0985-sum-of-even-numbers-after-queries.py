class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumAll = sum(filter(lambda x: x % 2 == 0, nums))
        ret = []
        for (k,v) in queries:
            if(nums[v] % 2 == 0):
                # 계산전 짝수면 빼두고
                sumAll -= nums[v]
            nums[v] += k
            if(nums[v] % 2 == 0):
                # 계산후 짝수면 다시 더함
                sumAll += nums[v]
            ret.append(sumAll)

        return ret
