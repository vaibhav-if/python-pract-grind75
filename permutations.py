class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return [[]]

        result = []
        for i in range(len(nums)):
            remaining_nums = nums[:i] + nums[i+1:]
            remaining_permutations = self.permute(remaining_nums)

            for permutation in remaining_permutations:
                result.append([nums[i]] + permutation)

        return result

sol = Solution()
print(sol.permute([1,2,3]))