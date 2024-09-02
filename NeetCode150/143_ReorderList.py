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

        dummy = ListNode()
        dummy.next = head
        res = dummy
        while prev and head:
            dummy.next = head
            head = head.next
            dummy = dummy.next
            
            dummy.next = prev
            prev = prev.next
            dummy = dummy.next

        if head:
            dummy.next = head

        return res.next
