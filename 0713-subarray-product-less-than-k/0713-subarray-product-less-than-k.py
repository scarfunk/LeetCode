from itertools import combinations

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:     
# TLE 로 실패.
#         win_size = 1
#         n = len(nums)
#         ret = 0
#         while win_size <= n:
#             for i in range(n+1-win_size): # winsize 가 1>4번, 2>3번
#                 subs = nums[i:i+win_size]
#                 # print(subs)
#                 mul = 1
#                 for x in subs:
#                     mul *= x
#                 if mul < k:
#                     # print(win_size, subs)
#                     # print("mul:", mul)
#                     ret += 1
#             win_size += 1
        
#         return ret

# 힌트참고 하여 재풀이
# [10, 5, 2, 6] 일때 4개 제외하고 (10,5), (5,2) (5,2,6) (2,6) 으로 총 8개
# right:0 10 > 1개
# right:1 5, (10,5) 2개
# right:2 10*5*2 로 left 이동(prod = 100/10 백) 로 하고. 2, (5,2) 2개
# right:3 5*2*6 으로 6, (5,2,6), (2,6) 3개
# 서브어레이 이므로 3개 [a,b,c] 3원소라면 c를 포함한 서브는 3개만 만들수 있다는 포인트 (c) (b,c) (a,b,c)

        prod = 1
        left = 0
        ret = 0
        
        for right in range(len(nums)):
            prod *= nums[right]
            if prod >= k:
                while prod >=k and left <= right:
                    prod /= nums[left]
                    left += 1
                    
            ret += right - left + 1
            
        return ret
        
        