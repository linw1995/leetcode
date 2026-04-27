# Created by 林玮 (Jade Lin) at 2026/04/27 08:58
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/

from typing import *
from leetgo_py import *


# Definition for a Node.
class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


# @lc code=begin


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if root is None:
            return 0

        if not root.children:
            return 1

        return max(self.maxDepth(child) + 1 for child in root.children)


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: int = deserialize("int", read_line())
    ans = Solution().maxDepth(root)
    print("\noutput:", serialize(ans, "integer"))
