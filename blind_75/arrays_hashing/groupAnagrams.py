# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order. An Anagram is a
# word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.

from typing import List
import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


class Solution:
    def groupAnagram(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        for st in strs:
            array = [0] * 26
            for l in st:
                array[ord(l) - ord("a")] += 1
            hmap[tuple(array)].append(st)
        return hmap.values()
