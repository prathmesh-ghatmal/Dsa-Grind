class Solution:
    def pattern_half_diamond(self, N):
        for i in range(1, 2 * N):  # outer loop (rows)
            
            # Step 1: find how many stars
            if i <= N:
                stars = i
            else:
                stars = 2 * N - i

            # Step 2: find how many spaces
            spaces = N - stars

            # Step 3: print spaces
            for s in range(spaces):
                print(" ", end="")

            # Step 4: print stars
            for j in range(stars):
                print("*", end="")

            # Step 5: move to next line
            print()


# Driver code
sol = Solution()
sol.pattern_half_diamond(6)
