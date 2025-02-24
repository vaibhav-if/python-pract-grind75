class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        product = [0] * l

        prefix = 1
        for i in range(l):
            product[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(l-1, -1, -1):
            product[i] *= postfix
            postfix *= nums[i]

        return product

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))