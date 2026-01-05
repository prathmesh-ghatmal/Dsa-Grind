class Solution:
    def pattern5(self,n):
        for i in range(n):
            for j in range(n,i,-1):
                print(j , end="  ")
            print()

sol = Solution()
n = 5
sol.pattern5(n)
