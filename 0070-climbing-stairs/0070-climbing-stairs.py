class Solution:
    def climbStairs(self, n: int) -> int:
        # 2 => 2
        # 3 => 3
        # 4 => 1111 22 211 121 112 => 5개. 
        # -1 한것 -2 을 더해주면된다. 3+2 => 5
        
        # dict = defaultdict(int)
        dict = {}
        def recur(n):
            if n <= 1:
                return 1
            if n in dict:
                return dict[n]
            res = recur(n-1) + recur(n-2)
            dict[n] = res
            return res
        
        return recur(n)
        