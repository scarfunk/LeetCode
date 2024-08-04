class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l = len(nums)
        arr = []
        for i in range(0, l):
            cnt = 0
            for j in range(i, n):
                cnt += nums[j]
                arr.append(cnt)
        # print(arr)
        arr.sort()
        result = sum(arr[left-1:right])
        # print(result)
        return result % 1_000_000_007
        