# Created by 林玮 (Jade Lin) at 2026/04/17 08:51
# leetgo: 1.4.15
# https://leetcode.cn/problems/check-if-numbers-are-ascending-in-a-sentence/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        for word in s.split():
            if not word.isdigit():
                continue

            num = int(word)
            if num > prev:
                prev = num
            else:
                return False

        return True


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().areNumbersAscending(s)
    print("\noutput:", serialize(ans, "boolean"))
