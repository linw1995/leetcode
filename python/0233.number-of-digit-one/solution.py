# Created by 林玮 (Jade Lin) at 2026/03/10 17:28
# leetgo: 1.4.15
# https://leetcode.cn/problems/number-of-digit-one/

from typing import *
from leetgo_py import *

# @lc code=begin


from functools import cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0

        arr = []
        while n > 0:
            arr.append(n % 10)
            n //= 10

        @cache
        def dfs(cnt: int, pos: int, limit: bool) -> int:
            if pos < 0:
                return cnt

            ans = 0
            up = arr[pos] if limit else 9
            for i in range(up + 1):
                ans += dfs(cnt + 1 if i == 1 else cnt, pos - 1, limit and i == up)

            return ans

        return dfs(0, len(arr) - 1, True)

    # @lc code=end


if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countDigitOne(n)
    print("\noutput:", serialize(ans, "integer"))
