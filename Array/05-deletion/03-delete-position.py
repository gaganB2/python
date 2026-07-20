array = [2, 4, 6, 8, 10]
position=2
size = len(array)
index = position - 1
# find postion
for i in range(index,size-1):
    array[i] = array[i+1]
# array.pop()
size -= 1
# print(array[0:size])
for i in range(size):
    print(array[i])