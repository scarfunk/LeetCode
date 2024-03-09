class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        
        i = 0
        j = 0
        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                i = i + 1                
            elif nums1[i] > nums2[j]:
                j = j + 1
            else:
                return nums1[i] 

        return -1
            
        