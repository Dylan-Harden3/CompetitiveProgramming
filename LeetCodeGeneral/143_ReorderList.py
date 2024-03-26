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
        slow = fast = head

        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
                slow = slow.next
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n

        l1, l2 = head, prev
        while l1 and l2:
            l1n = l1.next
            l1.next = l2
            l2n = l2.next
            l2.next = l1n
            l1 = l1n
            l2 = l2n
