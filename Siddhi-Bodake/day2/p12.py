class Solution:
    def pattern12(self,n):
        spaces = 2*(n-1)
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end=" ")
            for j in range(spaces):
                print(" ", end=" ")
            for j in range(i, 0, -1):
                print(j, end=" ")
            spaces -= 2
            print()

sol = Solution()
n = 5
sol.pattern12(n)