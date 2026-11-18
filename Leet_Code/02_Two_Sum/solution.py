# LeetCode Problem: Two Sum

class Solution:

    def twoSum(self, nums, target):

        seen = {}

        for index, num in enumerate(nums):

            difference = target - num

            if difference in seen:
                return [seen[difference], index]

            seen[num] = index

nums = [2, 7, 11, 15]
target = 9

# Expected output: [0, 1]            