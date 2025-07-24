def permute(nums, start, end):
    if start == end:
        print(nums)
    
    for i in range(start, end):
        nums[start], nums[i] = nums[i], nums[start]
        permute(nums, start + 1, end)
        nums[start], nums[i] = nums[i], nums[start]

nums = [5, 3, 1, 8, 6, 2, 4]
permute(nums, 0, len(nums))