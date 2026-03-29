# Created by 林玮 (Jade Lin) at 2026/03/29 09:44
# leetgo: 1.4.15
# https://leetcode.cn/problems/check-if-strings-can-be-made-equal-with-operations-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        for i, c in enumerate(s1):
            if c == s2[i]:
                continue

            if i + 2 < n and c == s2[i + 2] and s1[i + 2] == s2[i]:
                continue

            if i - 2 >= 0 and c == s2[i - 2] and s1[i - 2] == s2[i]:
                continue

            return False

        return True


# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().canBeEqual(s1, s2)
    print("\noutput:", serialize(ans, "boolean"))
