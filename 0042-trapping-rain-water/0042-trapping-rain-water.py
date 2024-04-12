class Solution:
    def trap(self, hei: List[int]) -> int:
        res = 0
        left, right = 0, len(hei) - 1
        
        # 좌우 끝에서 가운데로 이동
        l_max, r_max = hei[left], hei[right]
        
        while left < right:
            
            # res 더하기 위해, 높은 위치를 기억하며 1 > 0 이면 1만큼
            l_max = max(l_max, hei[left])
            r_max = max(r_max, hei[right])
            
            # l,r 이 1개씩 줄지만, 가장높은 지점에서 한쪽에서 멈추도록.
            if l_max <= r_max:
                res += l_max - hei[left]
                left += 1
            else:
                res += r_max - hei[right]
                right -= 1
                
            
        return res
                
        