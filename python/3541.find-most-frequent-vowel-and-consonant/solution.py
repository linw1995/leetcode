# Created by 林玮 (Jade Lin) at 2026/02/23 17:15
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-most-frequent-vowel-and-consonant/

from typing import *
from leetgo_py import *

# @lc code=begin

from collections import Counter


class Solution:
    VOWELS = ["a", "e", "i", "o", "u"]

    def maxFreqSum(self, s: str) -> int:
        cnts = Counter(s)
        vowel_max = max(map(lambda k: cnts.get(k) or 0, self.VOWELS))
        others = [v for k, v in cnts.items() if k not in self.VOWELS]
        return vowel_max + (max(others) if others else 0)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maxFreqSum(s)
    print("\noutput:", serialize(ans, "integer"))
