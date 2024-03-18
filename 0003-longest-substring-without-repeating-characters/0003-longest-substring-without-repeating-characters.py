class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = {}
        start = 0
        max_len = 0
        for i in range(len(s)):
            curr_char = s[i]
            # 이미 등장한 문자라면 start 를 이전것보다 1개 뒤로.
            # 윈도우바깥(이전) 에 있는것은 else 로 타도록.
            if curr_char in mem and mem[curr_char] >= start:
                start = mem[curr_char] + 1
            else: # 첫등장 문자면 max_len 갱신
                max_len = max(max_len, i - start + 1)
            mem[s[i]] = i # 문자의 마지막 인덱스
        # print(mem)
        return max_len