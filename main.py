import math

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

file = open("baseballdata.txt", "r")

actual = []
expected = []

for line in file:
    line = line.split("\t")
    actual.append(float(line[6]))
    expected.append(1 / (1 + pow(float(line[8]) / float(line[7]), 2))) #Use pythagorean approximation to find expected win%

print(pearson_def(actual, expected))