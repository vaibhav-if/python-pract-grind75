class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [] 
    
        def backtrack(start, current_subset):
            result.append(current_subset[:]) 
            
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
        
        backtrack(0, [])
        return result

sol = Solution()
print(sol.subsets([3,2,4,1]))