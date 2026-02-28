# Created by 林玮 (Jade Lin) at 2026/02/28 10:58
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-the-digits-that-divide-a-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        step = 1

        while True:
            divder = (num // step) % 10
            if divder <= 0:
                break

            if num % divder == 0:
                ans += 1

            step *= 10

        return ans


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().countDigits(num)
    print("\noutput:", serialize(ans, "integer"))
