
# LeetCode #242 - Valid Anagram

from collections import Counter


class Solution:

    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)


solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))  # True
print(solution.isAnagram("rat", "car"))          # False
