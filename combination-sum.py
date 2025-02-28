class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(combination, remaining_target, start_index):
            if remaining_target == 0:
                result.append(combination[:])
                return
            elif remaining_target < 0:
                return

            for i in range(start_index, len(candidates)):
                combination.append(candidates[i])
                backtrack(combination, remaining_target - candidates[i], i)
                combination.pop()

        backtrack([], target, 0)
        return result
                

sol = Solution()
print(sol.combinationSum([2,3,5], 8))