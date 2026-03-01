# Created by 林玮 (Jade Lin) at 2026/03/01 14:27
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-mode-in-binary-search-tree/

from typing import *
from leetgo_py import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=begin

from collections import Counter


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnts = Counter(self.iterNode(root))
        ans = []
        target = 0
        for v, cnt in cnts.most_common():
            if cnt < target:
                break

            target = cnt
            ans.append(v)

        return ans

    def iterNode(self, node: Optional[TreeNode]) -> List[int]:
        if node is None:
            return []

        return [node.val] + self.iterNode(node.left) + self.iterNode(node.right)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().findMode(root)
    print("\noutput:", serialize(ans, "integer[]"))
