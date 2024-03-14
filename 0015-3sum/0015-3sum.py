class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 올림차순 소팅을 한다
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)):
            # 고정시키고 나머지를 투포인터 좁히기로 찾는다.
            fix = nums[i]
            tmp = nums[i+1:]
            left = 0
            right = len(tmp) - 1 

            # 중복패스
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while left < right:
                sum = fix + tmp[left] + tmp[right]
                if sum == 0:
                    result.append([fix, tmp[left], tmp[right]])
                    # 중복패스
                    while left < right and tmp[left] == tmp[left+1]:
                        left += 1
                    while left < right and tmp[right] == tmp[right-1]:
                        right -= 1

                    right -= 1
                    left += 1
                elif sum > 0: # 소팅 되있으므로 우측을 내려야 음수가 된다.
                    right -= 1
                else:
                    left += 1
            
        # print(result)
        return result
            