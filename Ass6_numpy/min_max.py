import numpy
import numpy
N, M = map(int, input().split())

A = numpy.array([input().split() for i in range(N)],dtype = int)
print(numpy.max(numpy.min(A, axis=1), axis=0))