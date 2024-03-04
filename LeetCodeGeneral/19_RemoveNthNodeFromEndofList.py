# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        prev = None
        size = 1
        while cur.next:
            prev = cur
            cur = cur.next
            size += 1

        if size == n:
            return head.next

        cnt = 0
        cur = head
        prev = None
        while cnt < size - n:
            prev = cur
            cur = cur.next
            cnt += 1

        if not prev: return None
        prev.next = cur.next

        return head
