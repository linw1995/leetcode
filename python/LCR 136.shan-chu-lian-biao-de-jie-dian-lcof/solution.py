# Created by 林玮 (Jade Lin) at 2026/03/30 10:02
# leetgo: 1.4.15
# https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/

from typing import *
from leetgo_py import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=begin


class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return

        dummy = ListNode(val=-1, next=head) # dummy
        prev = dummy
        node = dummy.next
        while node is not None:
            if node.val == val:
                prev.next = node.next
                return dummy.next

            prev = node
            node = node.next

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    val: int = deserialize("int", read_line())
    ans = Solution().deleteNode(head, val)
    print("\noutput:", serialize(ans, "ListNode"))
