/*
 * @lc app=leetcode.cn id=1 lang=c
 *
 * [1] 两数之和
 *
 * https://leetcode-cn.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (46.74%)
 * Likes:    7307
 * Dislikes: 0
 * Total Accepted:    756.8K
 * Total Submissions: 1.6M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * 给定一个整数数组 nums 和一个目标值
 * target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
 *
 * 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
 *
 * 示例:
 *
 * 给定 nums = [2, 7, 11, 15], target = 9
 *
 * 因为 nums[0] + nums[1] = 2 + 7 = 9
 * 所以返回 [0, 1]
 *
 *
 */

// @lc code=start

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *twoSum(int *nums, int numsSize, int target, int *returnSize) {
  int *rv = malloc(sizeof(int) * 2);
  *returnSize = 2;
  for (rv[0] = 0; rv[0] < numsSize; rv[0]++) {
    for (rv[1] = rv[0] + 1; rv[1] < numsSize; rv[1]++) {
      if (nums[rv[0]] + nums[rv[1]] == target) {
        return rv;
      }
    }
  }
  *returnSize = 0;
  return rv;
}

// @lc code=end
