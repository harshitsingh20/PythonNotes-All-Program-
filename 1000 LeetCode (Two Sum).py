# Brute force algorithm: - This means that solve the given problem in any time and space complexity

# brute force Solution

# class Solution:
#     def twoSum(self, nums,target):
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                            sum = nums[i] +nums[j]
#                            if sum == target:
#                                 return [i,j]


# O(n) Complexity :- Best case Complexity

class Solution:
    def twoSum(self, nums,target):
        dict={}
        for index,n in enumerate(nums): # n stores the value of index
            if n in dict:
                return [dict[n],index]
            else:
                dict[target-n]=index