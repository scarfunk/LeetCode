class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last = s.split(" ")[-1]
        return len(last)