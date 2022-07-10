# Solution 1(Itrative Solution)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# #         Time Comp = O(n)
# #         Memory Comp = O(1)
#         pre, curr = None, head
#         while curr:
#             nextt  = curr.next
#             curr.next = pre
#             pre = curr
#             curr = nextt
#         return pre