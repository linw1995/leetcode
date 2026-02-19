# Created by 林玮 (Jade Lin) at 2026/02/19 20:21
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-binary-substrings/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        expect = "0"

        prev = 0
        cur = 0
        for c in s:
            if c == expect:
                cur += 1
            else:
                expect = c
                cnt = min(prev, cur)
                ans += cnt
                prev = cur
                cur = 1

        cnt = min(prev, cur)
        if cnt > 0:
            ans += cnt

        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countBinarySubstrings(s)
    print("\noutput:", serialize(ans, "integer"))
