class Solution:
    def pattern6(self,n):
        for i in range(n):
            for j in range(n,i,-1):
                print(n-j+1 , end="  ")
            print()

sol = Solution()
n = 5
sol.pattern6(n)