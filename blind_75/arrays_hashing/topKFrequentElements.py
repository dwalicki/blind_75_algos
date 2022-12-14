# Given an integer array nums and an integer k, return
# the k most frequent elements.  You may return the answer in any order.

from collections import Counter

nums = [1, 1, 1, 2, 2, 3]
k = 2


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [num for num, _ in Counter(nums).most_common(k)]


test_solution = Solution()
test_solution.topKFrequent(nums, k)
