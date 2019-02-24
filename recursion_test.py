#recursion test
import math

def RecMethod(arr, index = 0):
    if math.sqrt(max(arr)) < arr[index]:
        return arr
    return RecMethod(list(filter(lambda x: x==arr[index] or x % arr[index] != 0, arr)), index + 1)

array = list(range(2, 10000))
print(RecMethod(array))
