# Created by 林玮 (Jade Lin) at 2026/03/12 15:24
# leetgo: 1.4.15
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import *
from leetgo_py import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=begin


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        idx = inorder.index(preorder[0])
        inorder_left = inorder[0:idx]
        preorder_left = preorder[1 : len(inorder_left) + 1]

        inorder_right = inorder[idx + 1 :]
        preorder_right = preorder[len(inorder_left) + 1 :]
        return TreeNode(
            val=preorder[0],
            left=self.buildTree(preorder_left, inorder_left),
            right=self.buildTree(preorder_right, inorder_right),
        )


# @lc code=end

if __name__ == "__main__":
    preorder: List[int] = deserialize("List[int]", read_line())
    inorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().buildTree(preorder, inorder)
    print("\noutput:", serialize(ans, "TreeNode"))
