# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        root = head
        carry = 0
        
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
                
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry, val  = sum // 10, sum % 10
            # 노드 생성해가면서 붙인다
            head.next = ListNode(val)
            head = head.next
            
        return root.next