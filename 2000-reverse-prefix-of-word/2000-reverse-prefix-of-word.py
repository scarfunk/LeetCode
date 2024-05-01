class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        return ''.join(reversed(word[:idx+1])) + word[idx+1:]