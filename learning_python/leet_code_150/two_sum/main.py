# Solution 1

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0, len(nums)):
#             for j in range(i, len(nums)):
#                 sum = nums[i] + nums[j]
#                 if sum == target:
#                     return[i, j]
#
# sum1 = Solution()
# num1 = [2, 7, 11, 15]
# target1 = 9
# result = sum1.twoSum(num1, target1)
# print(result[0], result[1])

# Solution 2

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seenNumbers = {}  # 2
#
#         for i in range(0, len(nums)):  # needNumber
#             needNumber = target - nums[i]  # 2
#             if needNumber in seenNumbers:
#                 print("returned with indexes:", seenNumbers[needNumber], i)
#                 return [seenNumbers[needNumber], i]
#             else:
#                 print(f"added with indexes:, {nums[i]}, {i}")
#                 seenNumbers[nums[i]] = i
#
#
# # 9 - 2 == 7
# # 9 - 7 = 2
# # 9 - 7= 2 -> 2 - 2 = 0
# sum1 = Solution()
# num1 = [2, 7, 11, 15]
# target1 = 9
# result = sum1.twoSum(num1, target1)
# print(result[0], result[1])
# two sum problem leetcode


# ht = {1:2}
# key, Value
# ht[1] = 2

# 2 11 7 11 15
# 9

# ht = {7:0, -2: 1, }
# # variable, index
# 7

