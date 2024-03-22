# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
        
        # print(fast)
        # print(slow)
        # print(reverse)

        if fast:
            slow = slow.next

        # slow 를 순방향 계속 진행시키면서 reverse 와 체크
        while reverse and reverse.val == slow.val:
            reverse, slow = reverse.next, slow.next
        
        return reverse is None