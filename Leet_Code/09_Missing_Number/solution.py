class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum


if __name__ == "__main__":
    solution = Solution()

    print(solution.missingNumber([3, 0, 1]))
    print(solution.missingNumber([0, 1]))
    print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))