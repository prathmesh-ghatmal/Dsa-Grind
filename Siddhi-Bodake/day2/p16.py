class Solution:
    def pattern16(self,n):
        for i in range(n):
            char = chr(65 + i)
            for j in range(i+1):
                print(char, end=" ")
            print()
sol = Solution()
n = 5
sol.pattern16(n)