# Created by 林玮 (Jade Lin) at 2026/03/27 21:55
# leetgo: 1.4.15
# https://leetcode.cn/problems/matrix-similarity-after-cyclic-shifts/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for idx, row in enumerate(mat):
            if idx % 2 == 0:
                if not self.rowSimilar(row, k):
                    return False
            else:
                if not self.rowSimilar(list(reversed(row)), k):
                    return False

        return True

    def rowSimilar(self, row: List[int], k: int) -> bool:
        n = len(row)
        k %= n
        if k == 0:
            return True

        for idx, num in enumerate(row):
            if num != row[(idx + k) % n]:
                return False

        return True


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().areSimilar(mat, k)
    print("\noutput:", serialize(ans, "boolean"))
