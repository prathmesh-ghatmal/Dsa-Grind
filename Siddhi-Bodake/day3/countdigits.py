class Solution:
    def countDigits(self,n):
        count = 0
        if n == 0:
            return 1
        while n > 0:
            n = n//10
            count += 1
        return count
    
sol = Solution()
n = 12345876756
print(sol.countDigits(n))