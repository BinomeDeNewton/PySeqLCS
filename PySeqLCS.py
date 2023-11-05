# Longest Common Subsequence (LCS) between two strings

# Function D: Recursive approach without memoization
def D(i, j):
    if i == 0 or j == 0:
        return 0
    else:
        if x[i - 1] == y[j - 1]:
            return 1 + D(i - 1, j - 1)
        else:
            return max(D(i - 1, j), D(i, j - 1))

# Function I: Iterative approach
def I(x, y):
    # Size of the lists
    m = len(x)
    n = len(y)

    # Create a table to store the solved sub-problems
    L = [[0] * (n + 1) for i in range(m + 1)]

    # Fill the table L from bottom to top
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]

# Function LCS: Recursive approach with memoization
def LCS(x, y):
    if not x or not y:
        return ""
    elif x[-1] == y[-1]:
        return LCS(x[:-1], y[:-1]) + x[-1]
    else:
        lcs1 = LCS(x, y[:-1])
        lcs2 = LCS(x[:-1], y)
        return max(lcs1, lcs2, key=len)

# Function M: Memoization approach
def M(s1, s2):
    memo = {}

    def lcs_helper(i, j):
        if i == 0 or j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if s1[i - 1] == s2[j - 1]:
            memo[(i, j)] = 1 + lcs_helper(i - 1, j - 1)
        else:
            memo[(i, j)] = max(lcs_helper(i, j - 1), lcs_helper(i - 1, j))
        return memo[(i, j)]

    length = lcs_helper(len(s1), len(s2))
    result = [''] * length

    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result[length - 1] = s1[i - 1]
            i -= 1
            j -= 1
            length -= 1
        elif memo.get((i - 1, j), 0) > memo.get((i, j - 1), 0):
            i -= 1
        else:
            j -= 1

    return ''.join(result)

# Sample strings
x = "aauadd"
y = "hubbbdbbdb"
z = "aaddouih"

# Displaying results
print("Results of D, I, LCS, and M functions for the following strings:")
print(f"String 1: {x}")
print(f"String 2: {y}")
print(f"String 3: {z}")
print("--------------------")
print("--------------------")
print("For the Iterative function (I):")
print(I(x, y))
print(I(x, z))
print()
print("--------------------")
print("--------------------")
print("For the Recursive function by the Professor (D):")
print(D(len(x), len(y)))
print(D(len(x), len(z)))
print()
print("--------------------")
print("--------------------")
print("For the Recursive function (LCS) by Me:")
print(LCS(x, y))
print(LCS(x, z))
print()
print("--------------------")
print("--------------------")
print("For the Memoization function (M):")
print(M(x, y))
print(M(x, z))
print()
print("--------------------")
print("--------------------")
