class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0
        j = 0
        while(i < len(g) and j < len(s)):
            if g[i] > s[j]:
                j = j + 1
            else:
                i = i + 1
                j = j + 1
        
        print(i)
        return i
        