class Solution:
    # Function to print Pattern 20
    def pattern20(self, n):
        # Initialize spaces between star blocks
        spaces = 2 * n - 2

        # Loop for rows
        for i in range(1, 2 * n):
            # Calculate stars for first half
            stars = i

            # Adjust stars for second half
            if i > n:
                stars = 2 * n - i

            # Print left stars
            print("*" * stars, end="")

            # Print spaces
            print(" " * spaces, end="")

            # Print right stars
            print("*" * stars)

            # Adjust spaces for next row
            if i < n:
                spaces -= 2
            else:
                spaces += 2


if __name__ == "__main__":
    # Create solution object
    sol = Solution()
    # Define N
    N = 5
    # Call pattern function
    sol.pattern20(N)
