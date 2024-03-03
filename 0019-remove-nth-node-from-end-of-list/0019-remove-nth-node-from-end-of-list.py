# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        copy = head
        ptr = head
        fwd = 0

        # copy 를 n 만큼 먼저이동시킨다.
        for i in range(n):
            copy = copy.next
        # n 이 목록길이와 같으면. 첫노드가 제거 대상이다. 
        # n = 뒤에서 부터 n 번째를 제거
        if copy is None:
            return head.next
        # 포인터를 같이 증가 이동.
        while(copy.next):
            copy = copy.next
            ptr = ptr.next
        # n 번쨰 요소 1개만을 지운다.
        ptr.next = ptr.next.next
        return head