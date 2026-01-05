class Solution:
    def pattern91(self,n):
        for i in range(n):
            print(" "*(n-i-1), end="")
            print("*" *(2*i+1), end="") 
            print(" "*(n-i-1))

    def pattern92(self,n):
        for i in range(n):
            print(" " * i, end="")
            print("*" * (2*n - (2*i + 1)), end="")
            print(" " * i)

sol = Solution()
n = 5
sol.pattern91(n)
sol.pattern92(n)