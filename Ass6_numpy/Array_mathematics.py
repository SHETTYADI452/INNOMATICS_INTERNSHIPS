import numpy
def array_operations( arr1, arr2):
    add = numpy.add(arr1,arr2)
    sub = numpy.subtract(arr1, arr2)
    mul = numpy.multiply(arr1, arr2)
    div = arr1//arr2
    mod = numpy.mod(arr1, arr2)
    power = numpy.power(arr1, arr2)
    return add,sub,mul,div,mod,power


N, M = map(int, input().split())

arr1 = numpy.array([list(map(int, input().split())) for n in range(N)])
arr2 = numpy.array([list(map(int, input().split())) for n in range(N)])

add,sub,mul,div,mod,power = array_operations( arr1, arr2)
print(add)
print(sub)
print(mul)
print(div)
print(mod)
print(power)