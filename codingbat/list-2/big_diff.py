def big_diff(nums):
  nums.sort()
  return nums[len(nums)-1] - nums[0]