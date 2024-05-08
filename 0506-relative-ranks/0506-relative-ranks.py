class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        iv = list(enumerate(score))
        
        iv.sort(key = lambda x : -x[1])
        
        # print(iv)
        
        arr = [None] * len(score)
        for i in range(len(iv)):
            if i == 0:
                arr[iv[i][0]] = "Gold Medal"
                
            elif i == 1:
                arr[iv[i][0]] = "Silver Medal"
                
            elif i == 2:
                arr[iv[i][0]] = "Bronze Medal"
            else:  
                arr[iv[i][0]] = str(i+1)
                
        return arr
                
            
            
                
        
            