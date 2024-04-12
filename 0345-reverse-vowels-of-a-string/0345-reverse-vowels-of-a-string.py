class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        
        vo = ["a","e","i","o","u", "A", "E","I","O","U"]
        stk = []
        for c in s:
            if c in vo:
                while s[right] not in vo:
                    right -= 1
                stk.append(s[right])
                right -= 1
            else:
                stk.append(c)
                
        # print(stk)
        return "".join(stk)