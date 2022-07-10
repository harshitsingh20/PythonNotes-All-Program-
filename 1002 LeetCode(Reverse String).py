# Solution 1

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         left = 0
#         right = len(s)-1
#         while left<right:
#             temp = s[left]
#             s[left] = s[right]
#             left = left + 1
#             s[right] = temp
#             right = right -1


# Solution 2

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         left = 0
#         right = len(s)-1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left, right = left+1, right-1