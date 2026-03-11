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
        cntA = self.getLength(headA)
        cntB = self.getLength(headB)

        if cntA < cntB:
            headA, headB = headB, headA
            cntA, cntB = cntB, cntA

        pa, pb = headA, headB
        n = cntA - cntB
        while n > 0:
            pa = pa.next
            n -= 1

        while pa != pb:
            pa = pa.next
            pb = pb.next

        return pa

    def getLength(self, head: ListNode):
        cnt = 0
        p = head
        while p:
            p = p.next
            cnt += 1
        return cnt


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
