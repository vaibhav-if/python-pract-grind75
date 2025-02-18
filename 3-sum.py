def threeSum(nums: list[int]) -> list[list[int]]:
    if len(nums) == 3:
        return [nums] if sum(nums) == 0 else []
    
    length = len(nums)
    result = []

    nums.sort()

    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left = i + 1
        right = length - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while nums[left] == nums[left+1] and left < right - 1:
                    left += 1
                while nums[right] == nums[right-1] and left < right - 1:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

print(threeSum([0,0,0,0]))