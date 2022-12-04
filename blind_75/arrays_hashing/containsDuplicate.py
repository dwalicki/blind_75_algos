# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

from typing import List

nums = [1, 2, 3, 4]
nums2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return False
            nums_set.add(i)

        return True


test_solution = Solution()
print(test_solution.containsDuplicate(nums2))
