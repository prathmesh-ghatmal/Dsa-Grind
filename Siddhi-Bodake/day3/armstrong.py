def isArmstrong(n):
    # Step 1: Find the number of digits
    num_digits = len(str(n))
    
    # Step 2: Initialize sum
    total = 0
    temp = n  # make a copy so we can modify it
    
    # Step 3: Extract digits and calculate powered sum
    while temp > 0:
        digit = temp % 10          # get last digit
        total += digit ** num_digits  # add its power
        temp //= 10                # remove last digit
    
    # Step 4: Check if sum equals original number
    return total == n


# Driver code
N = 153
if isArmstrong(N):
    print(N, "is an Armstrong number ✅")
else:
    print(N, "is NOT an Armstrong number ❌")
