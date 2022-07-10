# Solution 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         nums = []
#         while head:
#             nums.append(head.val)
#             head = head.next
#         l, r = 0, len(nums)-1
#         while l<=r:
#             if nums[l] != nums[r]:
#                 return False
#             l = l + 1
#             r = r - 1
#         return True

# Solution 2 (Best Case)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         fast = head
#         slow = head
# #         Find Middle(Slow)
#         while fast and fast.next:
#             fast = fast.next.next
#             slow  = slow.next
# #             Reverse the Second Half
#         pre = None
#         while slow:
#             temp = slow.next
#             slow.next = pre
#             pre = slow
#             slow = temp
# #             Check the Palindrome Number
#         left, right = head, pre
#         while right:
#             if left.val != right.val:
#                 return False
#             left = left.next
#             right = right.next
#         return True