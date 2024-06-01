class Solution:
    def scoreOfString(self, arr: str) -> int:
        ret = 0
        for i in range(0, len(arr)-1):
            ret += abs(ord(arr[i]) - ord(arr[i+1]))
            
        return ret