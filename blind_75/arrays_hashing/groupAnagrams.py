# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order. An Anagram is a
# word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.

from typing import List
from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


class Solution:
    def groupAnagram(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26  # a.....z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()

        # O(m * n) - m = number of words given, n = length of each word


test_solution = Solution()
test_solution.groupAnagram(strs)
