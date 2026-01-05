class Solution:
    def isPrime(self, n):
        # Step 1: Special case: numbers <= 1 are not prime
        if n <= 1:
            return False

        # Step 2: Count divisors
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:  # if i divides n
                count += 1

        # Step 3: Check if it has exactly two divisors
        return count == 2


# Driver code
sol = Solution()
N = 7
if sol.isPrime(N):
    print(N, "is a Prime Number ✅")
else:
    print(N, "is NOT a Prime Number ❌")
