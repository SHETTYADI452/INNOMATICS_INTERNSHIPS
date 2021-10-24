import numpy

numpy.set_printoptions(sign=' ')

N, M = map(int, input().split())
eye = numpy.eye(N, M)
print(eye)