class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mem1 = {}
        mem2 = {}
        for i in range(len(s)):
            x, y = s[i], t[i]
            
            if x in mem1:
                if mem1[x] != y: return False
                
            if y in mem2:
                if mem2[y] != x: return False
                
            mem1[x] = y
            mem2[y] = x
        
        return True
            