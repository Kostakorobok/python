# https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution:  # 1, 2, 3, 4
    def runningSum(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)  # how much elems we got from nums
        result[0] = nums[0]

        for i in range(1, len(result)):
            result[i] = nums[i] + result[i - 1]

        return result

    def runningSum1(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)

        for i in range(len(nums)):
            for j in range(i + 1):
                result[i] += nums[j]

        return result

s = Solution()
print(s.runningSum1([1, 2, 3, 4]))