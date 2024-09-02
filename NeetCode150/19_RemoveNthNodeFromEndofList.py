# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0
        cur = head
        while cur:
            list_length += 1
            cur = cur.next

        prev = None
        cur = head
        for i in range(list_length - n):
            prev = cur
            cur = cur.next

        if prev is None:
            if cur.next is None:
                return None
            return cur.next

        prev.next = cur.next
        return head
