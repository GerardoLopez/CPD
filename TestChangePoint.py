
import matplotlib.pyplot as plt

import numpy
import ChangePoint

def main():
    data = numpy.loadtxt('Sample_4298_Line_1852_LTDR_BB_NIR.txt')
    x = data[:,0];
    data = data[:,1]

    points = sorted(set(ChangePoint.ChangePoint(data, confidence=99.)))
    print points
    print
    for i, a in zip(points, numpy.split(data, points)):
        if len(a) == 0:
            continue
        print x[i], "==>", a

    plt.plot(x,data)
    for cp in points:
        l = plt.axvline(x=x[cp], color='r')

    plt.show()

if __name__ == "__main__":
    main()
