# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        fast = head.next.next
        slow = head.next

        while fast:
            if fast.next is None:
                return slow
            fast = fast.next.next
            slow = slow.next

        return slow