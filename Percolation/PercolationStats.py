import Percolation
import random

class PercolationStats:

	# perform independent trials on an n-by-n grid
	def __init__(self, n, trials):

		for i in range(0, trials):

			# initialize all sites to be blocked
			trial = Percolation(n)

			# repeat the following until the system percolates
			while not trial.percolates():

				# choose a site at random among all blocked sites
				i = random(0, n)
				j = random(0, n)

				if trial.isOpen(i, j) or trial.isFull(i,j):
					continue

				# open the site
				trial.open(i, j)

			print("p: " + trial.numberOfOpenSites()/(n*n))


stats = PercolationStats(5, 1)