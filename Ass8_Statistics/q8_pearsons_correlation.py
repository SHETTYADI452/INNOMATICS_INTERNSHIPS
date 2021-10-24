def calculateMean(x):
    return(sum(x) / len(x))

def calculateStandardDeviation(x, m):
    l = []
    for i in range(len(x)):
        l.append((x[i]-m)**2)
    return ((sum(l) / len(l)) ** 0.5)

def calculatePearsonCorrelationCoefficient(n, x, y, d):
    meanX = calculateMean(x)
    meanY = calculateMean(y)
    stddevX = calculateStandardDeviation(x, meanX)
    stddevY = calculateStandardDeviation(y, meanY)
    numerator = 0
    for i in range(n):
        numerator = numerator + ((x[i] - meanX) * (y[i] - meanY))
    print(round(numerator / (n * stddevX * stddevY), d))

n = int(input().strip())
x = list(map(float, input().strip().split(' ')))
y = list(map(float, input().strip().split(' ')))
calculatePearsonCorrelationCoefficient(n, x, y, 3)