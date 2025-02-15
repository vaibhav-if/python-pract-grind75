def majorityElement(nums: list[int]) -> int:
    if len(nums) == 1 or len(nums) == 2:
        return nums[0]

    count_map = {}
    for n in nums:
        count_map[n] = count_map.get(n, 0) + 1

    return max(count_map, key=count_map.get)

print(majorityElement([2,2,2,1,1,2,2]))