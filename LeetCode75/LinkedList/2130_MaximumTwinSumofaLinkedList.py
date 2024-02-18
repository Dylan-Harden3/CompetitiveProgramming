# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next

        prev = None
        while slow:
            cur = slow.next
            slow.next = prev
            prev = slow
            slow = cur

        maxSum = 0
        while prev and head:
            maxSum = max(maxSum, prev.val + head.val)
            prev = prev.next
            head = head.next
            
        return maxSum
