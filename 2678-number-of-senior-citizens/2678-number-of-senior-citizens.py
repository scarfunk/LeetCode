class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for d in details:
            x = d[11:13]
            if int(x) > 60:
                cnt += 1
        return cnt