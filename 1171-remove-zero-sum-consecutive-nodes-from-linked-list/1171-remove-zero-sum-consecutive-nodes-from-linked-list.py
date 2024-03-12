# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 시작점 준비
        x = ListNode(0)
        x.next = head

        dummy = x

        sum = 0
        dict = {}
        while dummy:
            sum += dummy.val
            # 키를 합산. 값을 노드로 저장.
            # 1,3,-3,99 이면 {1:0n, 4:1n} > {1:2n, 4:1n}
            dict[sum] = dummy
            dummy = dummy.next

        sum = 0
        dummy = x
        while dummy:
            sum += dummy.val
            # {1:2n, 4:1n} 에서 0n.next = 2n.next 를 연결함.
            dummy.next = dict[sum].next
            # 다음루프는 2n.next = 3n(99) 가 된다.
            dummy = dummy.next
        return x.next

            