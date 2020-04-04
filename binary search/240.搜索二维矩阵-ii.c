/*
 * @lc app=leetcode.cn id=240 lang=c
 *
 * [240] 搜索二维矩阵 II
 *
 * https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
 *
 * algorithms
 * Medium (37.71%)
 * Likes:    261
 * Dislikes: 0
 * Total Accepted:    49.7K
 * Total Submissions: 125K
 * Testcase Example:
 '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n'
 + '5'
 *
 * 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值
 target。该矩阵具有以下特性：
 *
 *
 * 每行的元素从左到右升序排列。
 * 每列的元素从上到下升序排列。
 *
 *
 * 示例:
 *
 * 现有矩阵 matrix 如下：
 *
 * [
 * ⁠ [1,   4,  7, 11, 15],
 * ⁠ [2,   5,  8, 12, 19],
 * ⁠ [3,   6,  9, 16, 22],
 * ⁠ [10, 13, 14, 17, 24],
 * ⁠ [18, 21, 23, 26, 30]
 * ]
 *
 *
 * 给定 target = 5，返回 true。
 *
 * 给定 target = 20，返回 false。
 *
 */

// @lc code=start
#include <stdbool.h>

#define __WITH_LOG__

#ifdef __WITH_LOG__
#include <stdio.h>
#define LOG(message, args...)                                                  \
  fprintf(stdout, "| %s:%d | " message "\n", __FUNCTION__, __LINE__, ##args)
#else
#define LOG(message, args...)
#endif

bool _searchMatrix(int **matrix, int rowBegin, int rowEnd, int colBegin,
                   int colEnd, int target) {

  LOG("rowBegin=%d rowEnd=%d colBegin=%d colEnd=%d", rowBegin, rowEnd, colBegin,
      colEnd);

  if (rowEnd - rowBegin <= 2 || colEnd - colBegin <= 2) {
    for (int row = rowBegin; row < rowEnd; ++row) {
      for (int col = colBegin; col < colEnd; ++col) {
        if (matrix[row][col] == target)
          return true;
      }
    }
    return false;
  }

  int rowMid = (rowBegin + rowEnd) / 2, colMid = (colBegin + colEnd) / 2;
  if (matrix[rowMid][colMid] > target) {
    if (_searchMatrix(matrix, rowBegin, rowMid, colBegin, colMid, target)) {
      return true;
    }
  } else if (matrix[rowMid][colMid] < target) {
    if (_searchMatrix(matrix, rowMid, rowEnd, colMid, colEnd, target)) {
      return true;
    }
  } else {
    return true;
  }

  return _searchMatrix(matrix, rowBegin, rowMid, colMid, colEnd, target) ||
         _searchMatrix(matrix, rowMid, rowEnd, colBegin, colMid, target);
}

bool searchMatrix(int **matrix, int matrixRowSize, int matrixColSize,
                  int target) {
  return _searchMatrix(matrix, 0, matrixRowSize, 0, matrixColSize, target);
}

// @lc code=end
