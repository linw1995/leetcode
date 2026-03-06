# Created by 林玮 (Jade Lin) at 2026/03/06 21:52
# leetgo: 1.4.15
# https://leetcode.cn/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if s[0] != "1":
            return False

        bp = False
        for c in s:
            if c != "1":
                # Mark breaking
                bp = True
            elif bp:
                # It is breaking before
                return False

        return True


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().checkOnesSegment(s)
    print("\noutput:", serialize(ans, "boolean"))
