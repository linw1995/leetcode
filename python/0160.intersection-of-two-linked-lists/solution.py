# Created by 林玮 (Jade Lin) at 2026/03/11 21:22
# leetgo: 1.4.15
# https://leetcode.cn/problems/intersection-of-two-linked-lists/

from typing import *
from leetgo_py import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=begin


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    intersectVal: int = deserialize("int", read_line())
    listA: ListNode = deserialize("ListNode", read_line())
    listB: ListNode = deserialize("ListNode", read_line())
    skipA: int = deserialize("int", read_line())
    skipB: int = deserialize("int", read_line())
    ans = Solution().getIntersectionNode(intersectVal, listA, listB, skipA, skipB)
    print("\noutput:", serialize(ans, "ListNode"))
