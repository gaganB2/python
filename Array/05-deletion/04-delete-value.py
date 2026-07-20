array = [2, 4, 6, 8, 10]
value = 6

size = len(array)
index = 0

# find value's index
for i in range(size-1):
    if value == array[i]:
        index = i
        print("found index", i)


for i in range(index, size-1):
    array[i]=array[i+1]

size -= 1

for i in range(size):
    print(array[i])