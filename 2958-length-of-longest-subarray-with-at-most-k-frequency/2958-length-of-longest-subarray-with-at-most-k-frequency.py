class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_dist = 0
        left = 0
        mem = {}
        for right in range(n):
            # 원소를 순회하며 k 개 만큼 cnt 될때까지 map 에 담는다.
            x = nums[right]
            if x in mem:
                mem[x] += 1
            else:
                mem[x] = 1
                
            # right map.val 이 k 를 넘을때, left+1 하고 map -1 해주고 계속 진행한다.
            # k=2 45 456 4 이면, right = 5 일때 조건을 타고, left 가 이동하며 idx 2 일때(2번째4) cnt 가 -1 되며 while 을 빠져나간다.
            while mem[x] > k:
                mem[nums[left]] -= 1
                left += 1
            max_dist = max(max_dist, right - left + 1)
        return max_dist