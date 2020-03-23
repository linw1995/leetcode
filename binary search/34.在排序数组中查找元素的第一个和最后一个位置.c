/*
 * @lc app=leetcode.cn id=34 lang=c
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 *
 * https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (37.72%)
 * Likes:    353
 * Dislikes: 0
 * Total Accepted:    74K
 * Total Submissions: 188.7K
 * Testcase Example:  '[5,7,7,8,8,10]\n8'
 *
 * 给定一个按照升序排列的整数数组 nums，和一个目标值
 * target。找出给定目标值在数组中的开始位置和结束位置。
 *
 * 你的算法时间复杂度必须是 O(log n) 级别。
 *
 * 如果数组中不存在目标值，返回 [-1, -1]。
 *
 * 示例 1:
 *
 * 输入: nums = [5,7,7,8,8,10], target = 8
 * 输出: [3,4]
 *
 * 示例 2:
 *
 * 输入: nums = [5,7,7,8,8,10], target = 6
 * 输出: [-1,-1]
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
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *searchRange(int *nums, int numsSize, int target, int *returnSize) {
  int loc = binarySearch(nums, numsSize, target);
  LOG("loc: %d", loc);
  int *rv = malloc(sizeof(int) * 2);
  *returnSize = 2;
  if (loc < 0) {
    rv[0] = -1;
    rv[1] = -1;
    return rv;
  }
  int low = loc;
  // find low value
  while (low >= 0) {
    LOG("low: %d", low);
    rv[0] = low;
    low = binarySearch(nums, low, target);
  }
  // find high value
  int high = loc;
  while (high >= 0) {
    LOG("high: %d", high);
    rv[1] = high;
    int begin = high + 1;
    int newHigh = binarySearch(nums + begin, numsSize - begin, target);
    high = newHigh >= 0 ? newHigh + begin : -1;
  }
  return rv;
}
int binarySearch(int *nums, int numsSize, int target) {
  int low = 0, high = numsSize, mid = (high + low) / 2;
  while (low < high) {
    LOG("low: %d, high: %d, mid: %d, val: %d", low, high, mid, nums[mid]);
    if (nums[mid] < target) {
      low = mid + 1;
    } else if (nums[mid] > target) {
      high = mid;
    } else {
      return mid;
    }
    mid = (high + low) / 2;
  }
  return -1;
}

// @lc code=end
