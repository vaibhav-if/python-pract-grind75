class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return  ""
        
        if len(s) == 2 and s[0] == s[1]:
            return s
        
        palindrome = ""

        for i in range(len(s)):
            odd_palindrome = self.find_longest_palindrome(s, i, i)
            even_palindrome = self.find_longest_palindrome(s, i, i+1)

            if len(odd_palindrome) > len(palindrome):
                palindrome = odd_palindrome
            if len(even_palindrome) > len(palindrome):
                palindrome = even_palindrome
                
        return palindrome
    
    def find_longest_palindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]

sol = Solution()
print(sol.longestPalindrome("babad"))