
import matplotlib.pyplot as plt

import numpy
import ChangePoint

from scipy.interpolate import interp1d

def Interpolate(X, Y):
    from scipy.interpolate import interp1d
    # Interpolate where there is no data
    indices = numpy.where(Y<>0.0)
    x_with_data = X[indices[0]]
    y = Y[indices[0]]

    # find the first and last values on X
    index_first_element = numpy.where(X == x_with_data[0])
    index_last_element = numpy.where(X == x_with_data[-1])
    new_x = X[index_first_element[0][0]:index_last_element[0][0]]

    f = interp1d(x_with_data, y)
    interpolated_data = f(new_x)

    return new_x, interpolated_data

def main():
    data = numpy.loadtxt('Sample_1485_Line_684_LTDR_BB_NIR.txt')
    #data = numpy.loadtxt('Reflectance_27.9017_-101.881.txt')
    x = data[:,0]
    data = data[:,1]
    #data = data[:,6]

    indices = numpy.where(data==0)
    plt.plot(x[indices], data[indices], 'o', color='#C0C0C0')

    indices = numpy.where(data<>0)
    plt.plot(x[indices], data[indices], 'x', color='#C0C0C0')
    plt.plot(x[indices], data[indices], color='#C0C0C0', lw=0.8, label='Daily BB non-BRDF adjusted refl')

    x_interp, y_interp = Interpolate(x, data)
    #plt.plot(x_interp, y_interp, 'b',  label='Interpolated daily BB non-BRDF adjusted refl')
    indices = numpy.where(y_interp<>0)
    LocalMin = (numpy.diff(numpy.sign(numpy.diff(y_interp[indices]))) > 0).nonzero()[0] + 1
    LocalMax = (numpy.diff(numpy.sign(numpy.diff(y_interp[indices]))) < 0).nonzero()[0] + 1
    plt.plot(x_interp[LocalMin], y_interp[LocalMin], 'black', lw=0.7,)
    plt.plot(x_interp[LocalMax], y_interp[LocalMax], 'g', lw=0.5,)

    print x_interp[LocalMin]
    print y_interp[LocalMin]

    # Default call: ChangePoint(data, confidence=95., iterations=1000)
    #points = sorted(set(ChangePoint.ChangePoint(y_interp[LocalMin], confidence=99.)))
    points = ChangePoint.ChangePoint(y_interp[LocalMin], confidence=99.)
    print points
    print
    for i, a in zip(points, numpy.split(y_interp, points)):
        if len(a) == 0:
            continue
        print x[i], "==>", a

    for cp in point:
        print cp
        index = numpy.where( y_interp == y_interp[LocalMin][cp+1]  )
        l = plt.axvline(x=x[index[0]], color='r')

    plt.show()

if __name__ == "__main__":
    main()

