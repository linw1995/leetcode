# Created by 林玮 (Jade Lin) at 2026/04/15 21:42
# leetgo: 1.4.15
# https://leetcode.cn/problems/shortest-distance-to-target-string-in-a-circular-array/

from typing import *
from leetgo_py import *

# @lc code=begin

from math import inf, isinf


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = +inf
        n = len(words)
        for index, word in enumerate(words):
            if target == word:
                if startIndex < index:
                    ans = min(ans, index - startIndex, startIndex + n - index)
                else:
                    ans = min(ans, startIndex - index, index + n - startIndex)

        if isinf(ans):
            ans = -1

        return ans


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    startIndex: int = deserialize("int", read_line())
    ans = Solution().closestTarget(words, target, startIndex)
    print("\noutput:", serialize(ans, "integer"))
