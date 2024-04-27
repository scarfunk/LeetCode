class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        r = s.split(" ")
        dict1 = {} # a : dog
        dict2 = {} # dog : a
        
        if len(r) != len(p): return False
        
        for i in range(len(p)):
            k = p[i]
            v = r[i]
            
            if k in dict1:
                if dict1[k] != v: return False
                
            if v in dict2:
                if dict2[v]!= k: return False
                
            dict1[k] = v
            dict2[v] = k
            
        return True
            