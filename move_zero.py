def moveZeros(nums):
    nonzero_index = 0

    for i in range(len(nums)):

        if nums[i] != 0:
            nums[i], nums[nonzero_index] = nums[nonzero_index], nums[i]
            nonzero_index += 1

nums = [0, 1, 0, 3, 12]
moveZeros(nums)
print(nums)
