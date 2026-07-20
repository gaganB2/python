array = [2, 4, 6, 8, 10]

n = len(array)

# Shift elements left
for i in range(0, n-1):
    array[i] = array[i+1]

n = n - 1   # decrease array size

# Print only valid elements
for i in range(n):
    print(array[i], end=" ")


