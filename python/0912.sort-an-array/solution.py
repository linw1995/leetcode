# Created by 林玮 (Jade Lin) at 2026/03/11 17:40
# leetgo: 1.4.15
# https://leetcode.cn/problems/sort-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

from random import randint


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def rand_partition(l: int, r: int):
            i = randint(l, r)
            nums[i], nums[r] = nums[r], nums[i]
            return partition(l, r)

        def partition(l: int, r: int) -> int:
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def quicksort(l: int, r: int):
            if l < r:
                p = rand_partition(l, r)
                quicksort(l, p - 1)
                quicksort(p + 1, r)

        quicksort(0, len(nums) - 1)
        return nums


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortArray(nums)
    print("\noutput:", serialize(ans, "integer[]"))
