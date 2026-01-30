# Created by 林玮 (Jade Lin) at 2026/01/30 10:47
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-common-value/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return -1

        if nums1[0] < nums2[0]:
            candidate = nums2.pop(0)
            q = nums1
            tmp = nums2
        else:
            candidate = nums1.pop(0)
            q = nums2
            tmp = nums1

        while q:
            t = q.pop(0)
            if t == candidate:
                return t
            elif t > candidate:
                candidate = t
                q, tmp = tmp, q

        return -1


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().getCommon(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
