# Created by 林玮 (Jade Lin) at 2026/02/25 15:54
# leetgo: 1.4.15
# https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        self.sort(arr, 0, len(arr) - 1)
        return arr

    def sort(self, arr: List[int], left: int, right: int):
        if left >= right or left < 0:
            return

        pivot_idx = self.partition(arr, left, right)
        self.sort(arr, left, pivot_idx - 1)
        self.sort(arr, pivot_idx + 1, right)

    def partition(self, arr: List[int], left: int, right: int) -> int:
        pivot = arr[right]
        i = left

        for j in range(left, right):
            if self.lessThan(arr[j], pivot):
                self.swap(arr, i, j)
                i += 1

        self.swap(arr, i, right)
        return i

    def swap(self, arr: List[int], i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    def lessThan(self, a: int, b: int) -> bool:
        cnt_a = a.bit_count()
        cnt_b = b.bit_count()
        if cnt_a < cnt_b:
            return True
        elif cnt_a == cnt_b:
            return a < b
        else:
            return False


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortByBits(arr)
    print("\noutput:", serialize(ans, "integer[]"))
