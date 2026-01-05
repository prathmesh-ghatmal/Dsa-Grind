class Solution:
    def patter1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="  ")
            print()

sol = Solution()
n = 4
sol.patter1(n)
