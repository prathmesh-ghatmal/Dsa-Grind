def pattern17(N):
    for i in range(N):  # loop for rows

        # 1️⃣ Print spaces before letters
        print(" " * (N - i - 1), end="")

        # 2️⃣ Start with 'A'
        ch = ord('A')

        # 3️⃣ Find middle of the hill
        breakpoint = (2 * i + 1) // 2

        # 4️⃣ Print letters for this row
        for j in range(1, 2 * i + 2):  # because we go from 1 to 2*i+1
            print(chr(ch), end="")

            if j <= breakpoint:
                ch += 1  # climb up the hill (A→B→C)
            else:
                ch -= 1  # go down the hill (C→B→A)

        # 5️⃣ Move to next line
        print()


# Driver code
pattern17(5)
