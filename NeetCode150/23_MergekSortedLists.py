# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        def merge(l1, l2):
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            if l1:
                dummy.next = l1
            if l2:
                dummy.next = l2
            return cur.next
        c = 0
        while len(lists) > 1:
            next_lists = []
            i = 0
            while 2 * i + 1 < len(lists):
                next_lists.append(merge(lists[2*i], lists[2*i+1]))
                i += 1
            if len(lists) % 2:
                next_lists.append(lists[-1])
            lists = next_lists
        return lists[0]
