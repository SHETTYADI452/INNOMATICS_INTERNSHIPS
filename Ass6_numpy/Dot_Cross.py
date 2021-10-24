import numpy
N = int(input())
A = numpy.array([input().split() for i in range(N)], dtype =int)
B = numpy.array([input().split() for i in range(N)], dtype =int)
C = numpy.dot(A,B)
print(C)