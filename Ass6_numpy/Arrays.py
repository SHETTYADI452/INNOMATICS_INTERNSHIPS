import numpy

def arrays(arr):
    # complete this function
    arr.reverse()
    new_arr = numpy.array(arr,float)
    return new_arr
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)