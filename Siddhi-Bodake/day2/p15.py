class Solution:
    def pattern15(self,n):
        for i in range(n):
            for j in range(n-i):
                print(chr(65 + j), end=" ")
            print()
sol = Solution()
n = 5           
sol.pattern15(n)