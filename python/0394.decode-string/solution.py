# Created by 林玮 (Jade Lin) at 2026/03/13 10:10
# leetgo: 1.4.15
# https://leetcode.cn/problems/decode-string/

from re import sub
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def decodeString(self, s: str) -> str:
        for i, c in enumerate(s):
            if c != "[":
                continue

            prefix = s[:i]
            subfix = s[i + 1 :]
            prefix, k = self.decodeK(prefix)
            cnt = 0
            for j, c in enumerate(subfix):
                if c == "[":
                    cnt += 1

                if c != "]":
                    continue

                if cnt > 0:
                    cnt -= 1
                    continue

                return (
                    prefix
                    + "".join([self.decodeString(s[i + 1 : i + j + 1])] * k)
                    + self.decodeString(s[i + j + 2 :])
                )

        return s

    def decodeK(self, s: str) -> Tuple[str, int]:
        for i, c in enumerate(s):
            if not c.isdigit():
                continue

            return s[:i], int(s[i:])

        return s, 0


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().decodeString(s)
    print("\noutput:", serialize(ans, "string"))
