class Solution:
    
    def compareVersion(self, v1: str, v2: str) -> int:
        def ignoreLeadingZero(str):
            v = str.lstrip("0")
            if v == "":
                return 0
            else:
                return int(v)
            
            
        arr1 = v1.split(".")
        arr2 = v2.split(".")
        
        i = 0
        while i < len(arr1) and i < len(arr2):
            if ignoreLeadingZero(arr1[i]) > ignoreLeadingZero(arr2[i]):
                return 1
            elif ignoreLeadingZero(arr1[i]) < ignoreLeadingZero(arr2[i]):
                print("-1")
                return -1
            i += 1
            
        
        if arr1[i:]:
            
            if "".join(arr1[i:]).lstrip("0") != "":
                return 1
            
        if arr2[i:]:
            print("".join(arr2[i:]).find("1"))
            if "".join(arr2[i:]).lstrip("0") != "":
                print("(2) -1")
                return -1
        
        return 0
    
        
            
    
        