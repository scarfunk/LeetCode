class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ret = 0
        for i in range(0, len(s) + 1 - 3):
            c = s[i:i+3]
            if len(set(c)) == 3:
                print(c)
                ret += 1
               
        return ret
        