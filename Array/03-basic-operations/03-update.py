arr = [2, 4, 6, 8, 10]
index = 2
new_value = 100

count = 0
for _ in arr:
    count += 1

if 0 <= index < count:
    print("Before:", arr)
    arr[index] = new_value
    print("After :", arr)
else:
    print("Invalid Index")