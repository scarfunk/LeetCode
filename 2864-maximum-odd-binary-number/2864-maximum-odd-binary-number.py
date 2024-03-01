class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        reversed = sorted(s, reverse=True)
        return "".join(reversed[1:] + reversed[:1])