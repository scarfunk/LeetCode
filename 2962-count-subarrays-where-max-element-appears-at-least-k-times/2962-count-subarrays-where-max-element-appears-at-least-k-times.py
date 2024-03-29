class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 카운트가 k 가 된곳에서 최소 k 수를 유지하도록 left를 이동시키고, left 의 idx 만큼 서브어레이를 만들수 있으니 그만큼 더한다.
        big = max(nums)
        n = len(nums)
        left = 0
        curr = 0
        result = 0
        
        for right in range(n):
            x = nums[right]
            
            if x == big: # big 을 찾으면 카운트
                curr += 1 
            while curr >= k: # 카운트가 k 이상이면, left 를 이동시키면서 k 보다 작을때까지를 찾음.
                if nums[left] == big:
                    curr -= 1
                left += 1
            
            result += left # left 수만큼 더함.
            
            # 1 3 2 3 3 이면
            # 1 3 2 3   루프에 3갯수 == 2 이므로 left 를 2개이동. 후 left idx = 2 (끝이 323 으로인걸로 만들수 있는게 2개)
            #     2 3 3 루프에 다시 갯수 2 이므로 left 를 2개 이동. left idx = 4 (끝이 33 으로인걸로 만들수 있는게 4개)
                
        return result
            