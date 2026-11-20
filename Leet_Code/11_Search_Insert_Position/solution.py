class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reversed_number = 0

        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10

        return original == reversed_number


if __name__ == "__main__":
    solution = Solution()

    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))