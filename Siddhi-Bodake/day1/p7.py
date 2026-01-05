class Solution:
    def pattern7(self,n):
    
        for i in range(n):
            for j in range(n-i-1):
                print(" " , end="  ")
            for j in range(2*i+1):
                print("*" , end="  ")
            for j in range(n-i-1):
                print(" " , end="  ")
            print()

sol = Solution()
n = 5
sol.pattern7(n)