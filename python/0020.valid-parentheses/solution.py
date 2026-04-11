# Created by 林玮 (Jade Lin) at 2026/04/11 20:32
# leetgo: 1.4.15
# https://leetcode.cn/problems/valid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if stack and self.matches(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)

        return not stack

    def matches(self, left, right) -> bool:
        return f"{left}{right}" in ("()", "[]", "{}")


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isValid(s)
    print("\noutput:", serialize(ans, "boolean"))
