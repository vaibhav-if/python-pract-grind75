def maxSubArray(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    max_sum = sum = nums[0]

    for n in nums[1:]:
        if (sum + n) < n:
            sum = n
        else:
            sum += n
        
        if sum > max_sum:
            max_sum = sum

    return max_sum

print(maxSubArray([-2,-1]))