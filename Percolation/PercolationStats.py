from Percolation import Percolation
import random
import statistics
import math

class PercolationStats:

	# perform independent trials on an n-by-n grid
	def __init__(self, n, trials):

		self.trials = trials
		self.sum = 0
		self.results = [0] * trials

		for t in range(0, trials):

			# initialize all sites to be blocked
			trial = Percolation(n)

			# repeat the following until the system percolates
			while not trial.percolates() and trial.openCount < (n*n):

				# choose a site at random among all blocked sites
				i = random.randint(0, n-1)
				j = random.randint(0, n-1)

				if trial.isOpen(i, j) and trial.isFull(i,j):
					continue

				# open the site and fill adjacent
				trial.open(i, j)

			# if all sites are open and the system doesn't percolate, there was a problem
			if not trial.percolates() and trial.openCount == (n*n):
				raise Exception("Error percolating. Something went wrong while connecting the sites. Please try again.")

			p = trial.numberOfOpenSites()/(n*n)

			print(str(t+1) + " p: " + str(trial.numberOfOpenSites()) + "/" + str(n*n) + " = " + str(p))

			self.sum += p
			self.results[i] = p

	# sample mean of percolation threshold
	def mean(self):
		mean = self.sum / self.trials
		return mean
		

	# sample standard deviation of percolation threshold
	def stddev(self):
		stddev = statistics.stdev(self.results)
		return stddev

	# low endpoint of 95% confidence interval
	def confidenceLo(self):
		return self.mean() - (1.96 * math.sqrt(statistics.stdev(self.results)) / math.sqrt(self.trials))

	def confidenceHi(self):
		return self.mean() + (1.96 * math.sqrt(statistics.stdev(self.results)) / math.sqrt(self.trials))

	def confidence(self):
		print("95% confidence interval = [" + str(self.confidenceLo()) + ", " + str(self.confidenceHi()) + "]")



stats = PercolationStats(5, 30)
print("mean = " + str(stats.mean()))
print("stddev = " + str(stats.stddev()))
stats.confidence()