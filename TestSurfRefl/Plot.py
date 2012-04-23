
import matplotlib.pyplot as plt
import numpy
import sys

def main():
	file = sys.argv[1]

	data = numpy.loadtxt(file, skiprows=1, delimiter=',')
	#x = data[:,0]

	NumberOfBands = data.shape[1]

	for band in range(1,NumberOfBands):
		y = data[:,band]
		#plt.plot(x,y)
		plt.plot(y)

	plt.show()

if __name__ == "__main__":
    main()
