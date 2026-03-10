# Created by 林玮 (Jade Lin) at 2026/03/10 13:20
# leetgo: 1.4.15
# https://leetcode.cn/problems/existence-of-a-substring-in-a-string-and-its-reverse/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rs = "".join(reversed(s))
        for i, c in enumerate(s[:-1]):
            cc = s[i : i + 2]
            if cc in rs:
                return True

        return False


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isSubstringPresent(s)
    print("\noutput:", serialize(ans, "boolean"))
