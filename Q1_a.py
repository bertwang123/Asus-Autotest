def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

nums = [5, 3, 1, 8, 6, 2, 4]
bubbleSort(nums)
print(nums)