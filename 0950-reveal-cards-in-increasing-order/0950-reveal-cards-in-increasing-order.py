from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        # print(deck)
        
        que = deque([])
        while deck:
            if que:
                r = que.pop()
                que.appendleft(r)
            
            p = deck.pop()
            que.appendleft(p)
            # print(que)
            
        return list(que)
        
        
            