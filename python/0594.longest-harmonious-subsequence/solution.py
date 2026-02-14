# Created by 林玮 (Jade Lin) at 2026/02/14 10:36
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-harmonious-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # 哪两个相邻的数计数占比最多
        cnts = sorted([(num, cnt) for num, cnt in Counter(nums).most_common()])
        ans = 0
        for i, (a, cnt_a) in enumerate(cnts[:-1]):
            b, cnt_b = cnts[i + 1]
            if a - b == -1:
                ans = max(ans, cnt_a + cnt_b)

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findLHS(nums)
    print("\noutput:", serialize(ans, "integer"))
