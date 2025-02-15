class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique = set()

        for n in nums:
            if n in unique:
                return True
            
            unique.add(n)
        
        return False
    
s = Solution()
print(s.containsDuplicate([1,2,3,1]))