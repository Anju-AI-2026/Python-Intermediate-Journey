
# LeetCode #283 - Move Zeroes


class Solution:

    def moveZeroes(self, nums):

        position = 0

        for num in nums:

            if num != 0:
                nums[position] = num
                position += 1

        while position < len(nums):
            nums[position] = 0
            position += 1


solution = Solution()

numbers = [0, 1, 0, 3, 12]

solution.moveZeroes(numbers)

print(numbers)  # [1, 3, 12, 0, 0]
