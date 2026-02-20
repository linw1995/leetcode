# Created by 林玮 (Jade Lin) at 2026/02/20 17:52
# leetgo: 1.4.15
# https://leetcode.cn/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def modifyString(self, s: str) -> str:
        ans = []
        for idx, c in enumerate(s):
            if c == "?":
                prev = ans[-1] if ans else "z"
                next = s[idx + 1] if len(s) > idx + 1 else "z"
                nc = self.newChar(prev, next)
                ans.append(nc)
            else:
                ans.append(c)

        return "".join(ans)

    def newChar(self, prev: str, next: str) -> str:
        b = ord("a")
        prev_idx = ord(prev) - b

        next_idx = prev_idx
        if next != "?":
            next_idx = ord(next) - b

        idx = (prev_idx + 1) % 26
        if idx == next_idx:
            idx += 1

        return chr(idx % 26 + b)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().modifyString(s)
    print("\noutput:", serialize(ans, "string"))
