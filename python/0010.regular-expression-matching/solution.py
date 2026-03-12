# Created by 林玮 (Jade Lin) at 2026/03/12 16:38
# leetgo: 1.4.15
# https://leetcode.cn/problems/regular-expression-matching/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        if s and p[0] == ".":
            if len(p) > 1 and p[1] == "*":
                return (
                    self.isMatch(s[1:], p)
                    or self.isMatch(s[1:], p[2:])
                    or self.isMatch(s, p[2:])
                )

            return self.isMatch(s[1:], p[1:])
        elif len(p) > 1 and p[1] == "*":
            if s and p[0] == s[0]:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])

            return self.isMatch(s, p[2:])
        elif s and p[0] == s[0]:
            return self.isMatch(s[1:], p[1:])
        else:
            return False


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    ans = Solution().isMatch(s, p)
    print("\noutput:", serialize(ans, "boolean"))
