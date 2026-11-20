
# LeetCode #136 - Single Number


class Solution:

    def singleNumber(self, nums):

        result = 0

        for num in nums:
            result ^= num

        return result


solution = Solution()

print(solution.singleNumber([4, 1, 2, 1, 2]))  # 4
print(solution.singleNumber([2, 2, 1]))        # 1
