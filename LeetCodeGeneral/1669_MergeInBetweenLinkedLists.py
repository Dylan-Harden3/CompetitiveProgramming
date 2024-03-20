# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        diff = b-a+1
        head = list1

        while a:
            a -= 1
            if a:
                list1 = list1.next
        
        cur = list1.next
        while diff:
            diff -= 1
            cur = cur.next
        list1.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = cur
        return head
