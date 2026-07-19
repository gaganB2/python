array = [2, 4, 6, 8, 10]

value_to_insert = 5
array += [0] #create extra space

for i in range(len(array)-1,0,-1):
    print("Before: ",array[i]," <=>", array[i-1],"\n")
    array[i] = array[i-1]
    print("Before: ",array[i]," <=>", array[i-1])

array[0]=value_to_insert

print(array)