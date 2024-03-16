class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = [] # 스택에는 need to update 만 담는다. 담다가 1회만 업데이트 되는것이다.
        result = [0] * len(temp)
        for i, curr_t in enumerate(temp):
            
            # 스택이 있고 현재온도가 스택끝온도 보다 높으면
            while stack and curr_t > stack[-1][1]:
                set_idx, _ = stack.pop() # 지금보다 낮은 지점이다. 
                # 그리고 한번 셋팅이 되면 pop 되서 사라짐으로 재 업데이트 되지 않는다 1회만 업데이트 된다.
                # 2 > 3 > 1 > 4 라면 2 > 3 될때 2 는 pop 되서 할당된후 사라짐으로 2 > 4 차이때 2가 재 업데이트 될일은 없다(2>3으로 올라간 즉시 1회만 되는게 정답이니까)
                # 둘의 차를 이전 idx 에 넣는다.
                result[set_idx] = i - set_idx
            
            # 현재를 stack 에 넣고 또 다음을 비교한다.
            stack.append([i,curr_t])
            
        return result
                
            
        