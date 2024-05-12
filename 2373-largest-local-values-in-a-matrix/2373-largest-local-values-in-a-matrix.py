class Solution:
    def largestLocal(self, g: List[List[int]]) -> List[List[int]]:
        l = len(g)
        ret_len = l - 2
        ret = [[0] * ret_len for _ in range(ret_len)]
        
        for i in range(1, l-1):
            for j in range(1, l-1):
                # g[i][j] is center. find max with 9
                nine = g[i-1][j-1:j+2] + g[i][j-1:j+2] + g[i+1][j-1:j+2]
                print(nine)
                m = max(nine)

                ret[i-1][j-1] = m                
                
        return ret
            
            
        
        