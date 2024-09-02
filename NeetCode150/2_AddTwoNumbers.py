# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = 0

        def get_number(node):
            digit = 0
            res = 0
            while node:
                res += 10**digit*node.val
                digit += 1
                node = node.next
            return res

        res += get_number(l1) + get_number(l2)

        if res < 10:
            return ListNode(val=res)

        total_digits = len(str(res))
        cur = ListNode()
        sol = cur
        for i in range(total_digits):
            digit = res // (10**i) % 10
            cur.val = digit
            if i < total_digits-1:
                cur.next = ListNode()
                cur = cur.next

        return sol
