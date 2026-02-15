# Created by 林玮 (Jade Lin) at 2026/02/15 20:41
# leetgo: 1.4.15
# https://leetcode.cn/problems/add-binary/

from typing import *
from leetgo_py import *

# @lc code=begin

from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        arr_a = list(a)
        arr_b = list(b)
        ans = []

        incr = False
        for a, b in zip_longest(reversed(arr_a), reversed(arr_b)):
            if a == "1" and b == "1":
                ans.append("1" if incr else "0")
                incr = True
            elif a == "1" or b == "1":
                ans.append("0" if incr else "1")
            elif incr:
                ans.append("1")
                incr = False
            else:
                ans.append("0")

        if incr:
            ans.append("1")

        return "".join(reversed(ans))


# @lc code=end

if __name__ == "__main__":
    a: str = deserialize("str", read_line())
    b: str = deserialize("str", read_line())
    ans = Solution().addBinary(a, b)
    print("\noutput:", serialize(ans, "string"))
