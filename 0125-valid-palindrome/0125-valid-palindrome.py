class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]','', s)
        # print(s)
        s = s.lower()
        return s == s[::-1]
            