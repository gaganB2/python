array = [1,2, 3, 4, 5, 6, 7]

def recursive_loop(array, index):
    if index == len(array):
        return
    
    print(array[index])
    
    recursive_loop(array, index+1)


recursive_loop(array, 0)