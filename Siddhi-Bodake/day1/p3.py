class Solution:
    def patter3(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j , end="  ")
            print()

sol = Solution()
n = 4
sol.patter3(n)