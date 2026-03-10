# Created by 林玮 (Jade Lin) at 2026/03/10 22:10
# leetgo: 1.4.15
# https://leetcode.cn/problems/linked-list-cycle-ii/

from typing import *
from leetgo_py import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=begin


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        sp = head
        fp = head.next

        if fp is None:
            return None

        fp = fp.next
        while True:
            if fp is None:
                return None
            if sp == fp:
                break

            fp = fp.next
            if fp is None:
                return None
            if sp == fp:
                break
            fp = fp.next

            sp = sp.next

        p = sp.next
        length = 1
        while p != sp:
            p = p.next
            length += 1

        entry = head
        while length > 0:
            entry = entry.next
            length -= 1

        p = head
        while p != entry:
            p = p.next
            entry = entry.next

        return entry


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    pos: int = deserialize("int", read_line())
    ans = Solution().detectCycle(head, pos)
    print("\noutput:", serialize(ans, "ListNode"))
