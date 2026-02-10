# Created by 林玮 (Jade Lin) at 2026/02/10 14:34
# leetgo: 1.4.15
# https://leetcode.cn/problems/n-ary-tree-postorder-traversal/

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
    def postorder(self, root: "Node") -> List[int]:
        ans = []

        if root is None:
            return ans

        stack = [(root, False)]
        while stack:
            target, checked = stack.pop()
            if not checked and target.children is not None:
                stack.append((target, True))
                stack.extend(
                    reversed([(node, False) for node in target.children if node])
                )
            else:
                ans.append(target.val)

        return ans


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: int = deserialize("int", read_line())
    ans = Solution().postorder(root)
    print("\noutput:", serialize(ans, "integer[]"))
