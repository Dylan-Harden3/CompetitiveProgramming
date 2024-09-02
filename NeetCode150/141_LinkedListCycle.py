# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
    
        tortise = head
        hair = head.next

        for _ in range(10**9):
            if tortise == hair:
                return True
            
            if hair.next is None:
                return False
            hair = hair.next
            if tortise == hair:
                return True
            if tortise.next is None:
                return False
            tortise = tortise.next
            if tortise == hair:
                return True
            if hair.next is None:
                return False
            hair = hair.next
            if tortise == hair:
                return True
        return False
