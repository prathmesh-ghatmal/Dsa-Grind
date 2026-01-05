class Solution:
    def palindrome(self,n):
        rev = 0 
        dup = n
        while dup> 0:
            ld = dup%10
            rev = rev*10 + ld
            dup = dup//10
        if rev == n:
            return True
        else:
            return False
sol = Solution()
n = 121
print(sol.palindrome(n))