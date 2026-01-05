class Solution:
    # Function to print Pattern 18
    def pattern18(self, N):
        # Loop for each row
        for i in range(N):
            # Print characters from ('A' + N - 1 - i) to ('A' + N - 1)
            for ch in range(ord('A') + N - 1 - i, ord('A') + N):
                print(chr(ch), end=" ")
            # Move to next line after each row
            print()

if __name__ == "__main__":
    # Create solution object
    sol = Solution()
    # Define N
    N = 5
    # Call pattern function
    sol.pattern18(N)
