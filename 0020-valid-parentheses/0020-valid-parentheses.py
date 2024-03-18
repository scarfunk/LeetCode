class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mem = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        for c in s:
            if c in mem:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                d = stack.pop()
                if c != mem[d]:
                    return False
        
        if len(stack) > 0:
            return False
        return True
                    
        