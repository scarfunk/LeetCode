class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sec = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    sec += 1
                tickets[i] -= 1
                t = tickets[i]
            
                # print(i, tickets)
                if i == k and t == 0:
                    return sec

            