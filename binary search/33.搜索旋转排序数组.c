/*
 * @lc app=leetcode.cn id=33 lang=c
 *
 * [33] 搜索旋转排序数组
 *
 * https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (36.09%)
 * Likes:    564
 * Dislikes: 0
 * Total Accepted:    87.1K
 * Total Submissions: 238.7K
 * Testcase Example:  '[4,5,6,7,0,1,2]\n0'
 *
 * 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 *
 * ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
 *
 * 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
 *
 * 你可以假设数组中不存在重复的元素。
 *
 * 你的算法时间复杂度必须是 O(log n) 级别。
 *
 * 示例 1:
 *
 * 输入: nums = [4,5,6,7,0,1,2], target = 0
 * 输出: 4
 *
 *
 * 示例 2:
 *
 * 输入: nums = [4,5,6,7,0,1,2], target = 3
 * 输出: -1
 *
 */

// @lc code=start
#define __WITH_LOG__

#ifdef __WITH_LOG__
#include <stdio.h>
#define LOG(message, args...)                                                  \
  fprintf(stdout, "| %s:%d | " message "\n", __FUNCTION__, __LINE__, ##args)
#else
#define LOG(message, args...)
#endif
int search(int *nums, int numsSize, int target) {
  int low = 0, high = numsSize, mid = (high + low) / 2;
  while (low < high) {
    int newLow = low, newHigh = high;
    LOG("low %d, high %d, mid %d, val %d", low, high, mid, nums[mid]);
    if (nums[mid] < target) {
      newLow = mid + 1;
    } else if (nums[mid] > target) {
      newHigh = mid;
    } else {
      return mid;
    }

    if (nums[low] > nums[mid]) {
      LOG("Left part is unsorted");
      int rv = search(nums + low, mid - low, target);
      if (rv >= 0)
        return rv + low;
    }
    if (nums[mid] > nums[high - 1]) {
      LOG("Right part is unsorted");
      int rv = search(nums + mid, high - mid, target);
      if (rv >= 0)
        return rv + mid;
    }

    low = newLow;
    high = newHigh;
    mid = (low + high) / 2;
  }
  return -1;
}
// @lc code=end
