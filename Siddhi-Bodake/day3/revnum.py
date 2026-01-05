class Solution:
    def reverseNumber(self,n):
        rev=0
        while n> 0:
            ld = n%10
            rev = (rev *10)+ ld
            n = n//10
        return rev
sol = Solution()
n = 12345
print(sol.reverseNumber(n))