
import numpy
import unittest
from changepoint import changepoint
import matplotlib.pyplot as plt

#data = numpy.array([
#	10.7, 13.0, 11.4, 11.5, 12.5, 14.1, 14.8, 14.1,
#	12.6, 16.0, 11.7, 12.6, 13.0, 11.4,  7.9,  9.5,
#	8.0, 11.8, 10.5, 11.2,  9.2, 10.1, 10.4, 10.5,
#])

data = numpy.loadtxt('Reflectance_27.9017_-101.881.txt')
data = data[:,6]


class ChangepointTest(unittest.TestCase):

	def test_changepoint(self):
		x = numpy.arange(0, data.shape[0], 1);
		plt.plot(x,data)
		plt.show()

		cps = sorted(set(changepoint(data, confidence=90.)))
		print "First cps", cps

		self.assertEquals([10, 11], cps)
		cps = sorted(set(changepoint(data)))
		print "Second cps", cps
		self.assertEquals([11], cps)

if __name__ == "__main__":
	unittest.main()
