# An Anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase,
# typically using all the original letters exactly once.

s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"


class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


test_solution = Solution()
print(test_solution.validAnagram(s2, t2))
