class Solution:
    # Function to print Pattern 19
    def pattern19(self, N):
        # Initial spaces for upper half
        iniS = 0

        # Loop for upper half rows
        for i in range(N):
            # Print stars on left
            print("*" * (N - i), end="")
            # Print spaces in middle
            print(" " * iniS, end="")
            # Print stars on right
            print("*" * (N - i))
            # Increase middle spaces by 2
            iniS += 2

        # Initial spaces for lower half
        iniS = 2 * N - 2

        # Loop for lower half rows
        for i in range(1, N + 1):
            # Print stars on left
            print("*" * i, end="")
            # Print spaces in middle
            print(" " * iniS, end="")
            # Print stars on right
            print("*" * i)
            # Decrease middle spaces by 2
            iniS -= 2

if __name__ == "__main__":
    # Create solution object
    sol = Solution()
    # Define N
    N = 5
    # Call pattern function
    sol.pattern19(N)
