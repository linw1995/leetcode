# Created by 林玮 (Jade Lin) at 2026/02/07 10:23
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-number-of-pushes-to-type-word-i/

from typing import *
from leetgo_py import *

# @lc code=begin

from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        # 2 ~ 9, total: 8
        # a ~ z, total: 26
        cnts = Counter(word).most_common()
        return sum((no // 8 + 1) * cnt for no, (_, cnt) in enumerate(cnts))


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().minimumPushes(word)
    print("\noutput:", serialize(ans, "integer"))
