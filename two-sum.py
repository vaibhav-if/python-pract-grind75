def twoSum(nums: list[int], target: int) -> list[int]:
    numMap = {}
    l = len(nums)
    for i in range(l):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []


print(twoSum([2, 7, 11, 15], 9))