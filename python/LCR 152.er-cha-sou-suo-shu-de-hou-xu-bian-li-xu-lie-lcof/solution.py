# Created by 林玮 (Jade Lin) at 2026/03/13 11:05
# leetgo: 1.4.15
# https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j:
                return True

            # left tree
            p = i
            while postorder[p] < postorder[j]:
                p += 1

            # m is the start of right tree
            m = p

            while postorder[p] > postorder[j]:
                p += 1

            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


# @lc code=end

if __name__ == "__main__":
    postorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().verifyTreeOrder(postorder)
    print("\noutput:", serialize(ans, "boolean"))
