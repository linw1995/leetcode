#include "stdbool.h"
#include "uthash.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int id;
  UT_hash_handle hh;
} hashEntry;

bool setHas(hashEntry *set, int num) {
  hashEntry *s = NULL;
  HASH_FIND_INT(set, &num, s);
  return s != NULL ? true : false;
}

void setAdd(hashEntry **set, int num) {
  hashEntry *s = malloc(sizeof(hashEntry));
  s->id = num;
  HASH_ADD_INT(*set, id, s);
}

bool containsDuplicate(int *nums, int numsSize) {
  hashEntry *set = NULL;
  for (int i = 0; i < numsSize; ++i) {
    if (setHas(set, nums[i])) {
      return true;
    }
    setAdd(&set, nums[i]);
  }
  return false;
}

int main() {
  int nums[] = {1, 2, 3, 4, 5, 1};
  printf("%d\n", containsDuplicate(nums, 6));
}
