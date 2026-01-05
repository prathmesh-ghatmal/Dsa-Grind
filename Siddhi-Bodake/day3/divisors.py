class Solution:
    def getDivisors(self, N):
        res = []   # list to store divisors
        for i in range(1, N + 1):
            if N % i == 0:   # if i divides N completely
                res.append(i)
        return res


# Create object
sol = Solution()
N = 36
result = sol.getDivisors(N)
print("Divisors of", N, ":", *result)
