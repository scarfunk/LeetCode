class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        mem = {}
        ret = 0
        for w in words:
            if w in mem:
                ret += 1
            else:
                reversed = w[1]+w[0]
                mem[reversed] = 1
        return ret