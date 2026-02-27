# Created by 林玮 (Jade Lin) at 2026/02/27 20:27
# leetgo: 1.4.15
# https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        return password[target:] + password[:target]


# @lc code=end

if __name__ == "__main__":
    password: str = deserialize("str", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().dynamicPassword(password, target)
    print("\noutput:", serialize(ans, "string"))
