# Created by 林玮 (Jade Lin) at 2026/02/11 10:11
# leetgo: 1.4.15
# https://leetcode.cn/problems/special-positions-in-a-binary-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0

        for row in mat:
            if sum(row) != 1:
                continue

            col_idx = row.index(1)
            if sum(row[col_idx] for row in mat) == 1:
                ans += 1

        return ans


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numSpecial(mat)
    print("\noutput:", serialize(ans, "integer"))
