# Created by 林玮 (Jade Lin) at 2026/02/13 16:27
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range/

from typing import *
from leetgo_py import *

# @lc code=begin


VOWELS = frozenset(["a", "e", "i", "o", "u"])


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0

        for word in words[left : right + 1]:
            if word[0] in VOWELS and word[-1] in VOWELS:
                ans += 1

        return ans


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().vowelStrings(words, left, right)
    print("\noutput:", serialize(ans, "integer"))
