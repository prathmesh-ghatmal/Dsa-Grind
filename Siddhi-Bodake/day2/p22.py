class Solution:
    def pattern22(self, n):
        # Outer loop for rows
        for i in range(2 * n - 1):
            # Inner loop for columns
            for j in range(2 * n - 1):
                
                # Distances from each side
                top = i
                left = j
                bottom = (2 * n - 2) - i
                right = (2 * n - 2) - j

                # Smallest distance decides the layer
                minDist = min(top, bottom, left, right)

                # Number decreases as we go toward center
                print(n - minDist, end=" ")
            
            # Move to next row
            print()


sol = Solution()
n = 4
sol.pattern22(n)
