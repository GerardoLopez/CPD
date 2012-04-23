"""
Authors:   Gerardo Lopez-Saldana <GerardoLopez@isa.utl.pt>

This implementation is based on the algorithm documented at:
http://www.inference.phy.cam.ac.uk/rpa23/papers/rpa-changepoint.pdf.

A Matlab implementation can be found at:
http://www.cs.toronto.edu/~rpa/changepoint.shtml

"""
from __future__ import division

import numpy

def CuSum(data):
    Avg = numpy.average(data)
    m = numpy.zeros(len(data) + 1, dtype=float)
    # First element of cumulative sum is 0
    for i in range(1,len(data)):
        m[i] = m[i-1] + (data[i] - Avg)
    return m

def Bootstrap(data, iterations):
    c = CuSum(data)
    sdiff = c.max() - c.min()

    def Shuffled(x):
        y = numpy.array(x)
        numpy.random.shuffle(y)
        return y

    n = 0
    for i in range(iterations):
        b = CuSum(Shuffled(data))
        bdiff = b.max() - b.min()
        n += int(bdiff < sdiff)
    return float(n)

def ChangePoint(data, confidence=95., iterations=1000):
    c = CuSum(data)
    x = float(Bootstrap(data, iterations))
    p = (x/float(iterations)) * 100.0
    print p
    if p > confidence:
        #c = CuSum(data)
        mx = c.argmax()

	return mx, p
