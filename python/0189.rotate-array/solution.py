# Created by 林玮 (Jade Lin) at 2026/03/17 09:54
# leetgo: 1.4.15
# https://leetcode.cn/problems/rotate-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k %= size
        tmp = nums[: size - k]
        nums[:k] = nums[size - k :]
        nums[k:] = tmp


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    rotate(nums, k)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))
