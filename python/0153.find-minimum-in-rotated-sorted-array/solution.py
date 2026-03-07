# Created by 林玮 (Jade Lin) at 2026/03/07 23:29
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1

        return nums[low]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMin(nums)
    print("\noutput:", serialize(ans, "integer"))
