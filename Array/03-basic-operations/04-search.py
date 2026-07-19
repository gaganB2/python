array = [2, 4, 6, 8, 10]

target = 8

for index in range(len(array)):
     if array[index] == target:
          print("found at index: ", index)
          break
     
    #  else:
    #       print("value not present")
    # else will print if not found until target and breaks
