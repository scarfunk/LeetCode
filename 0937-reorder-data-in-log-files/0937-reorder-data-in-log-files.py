class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        alphas = []
        for l in logs:
            if l.split()[1].isalpha():
                alphas.append(l)
            else:
                digits.append(l)
        # print(alphas)
        alphas.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return alphas + digits


        