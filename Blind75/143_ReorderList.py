# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        
        while fast.next:
            fast = fast.next
            if fast.next:
                slow = slow.next
                fast = fast.next
        
        cur = slow.next
        slow.next = None
        slow = cur

        prev = None
        while slow:
            cur = slow.next
            slow.next = prev
            prev = slow
            slow = cur
        
        l1 = head
        l2 = prev

        while l1 and l2:
            cur1 = l1.next
            l1.next = l2
            cur2 = l2.next
            l2.next = cur1

            l1 = cur1
            l2 = cur2
        