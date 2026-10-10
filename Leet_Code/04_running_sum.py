# LeetCode #1480 - Running Sum of 1d Array

class Solution:

    def runningSum(self, nums):

        result = []
        total = 0

        for num in nums:

            total += num
            result.append(total)

        return result