class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            # 앞자리가 뒷자리보다 크면 제거.
            while k > 0 and len(stack) > 0 and stack[-1] > n:
                k -= 1
                stack.pop()
            stack.append(n)
            
        # print(stack)
        if k > 0:
            stack = stack[:-k]
        
        return "".join(stack).lstrip("0") or "0"