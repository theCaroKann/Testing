# get every triplet in nums array (different combination)
nums = [1, 2, 3, 4, 5]
for i in range(len(nums)): # index 0
  for j in range(i+1, len(nums)): # index 1 
    for k in range(j+1, len(nums)): # index 2
      print(nums[i], nums[j], nums[k])