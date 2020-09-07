import WeightedQuickUnionUF

class Site:
	def __init__(self, i):
		self.open = False
		self.val = i

class Percolation:
	
	# create n-by-n grid, with all sites initially blocked
	def __init__(self, n):

		if n <= 0:
			raise Exception("n must be greater than zero!")

		self.wqu = WeightedQuickUnionUF((n * n) + 2) # two extra values for virtual top and bottom sites

		self.grid = [None] * n # maintain grid representation separate from wqu list

		self.openCount = 0 # keep track of open sites

		# create grid with site objects
		for i in range(0, n):
			for j in range(0, n):
				# find the index of site in wqu
				value = (i * n) + j

				# assign site object to grid in closed and empty state
				site = Site(None)
				self.grid[i][j] = site

				# connect first row sites to top virtual site
				if i == 0:
					top = self.wqu[n * n] # top site is the second to last in wqu list
					self.wqu.union(val, top)

				# connect last row sites with bottom virtual site
				if i == n - 1:
					bottom = self.wqu[(n * n) - 1] # bottom site is the last in wqu list
					self.wqu.union(val, bottom)

	# opens the site (row, col) if it is not open
	def open(self, row, col):
		if row >= n or col >= n:
			raise Exception("Column or row index out of range!")
		if not self.isOpen(row, col):
			self.grid[row][col].open = True
			self.openCount += 1

	# is the site (row, col) open?
	def isOpen(self, row, col):
		if row >= n or col >= n:
			raise Exception("Column or row index out of range!")
		site = self.grid[row][col]
		if site.open:
			return True
		return False

	# is the site (row, col) full (or connected)?
	def isFull(self, row, col):
		if row >= n or col >= n:
			raise Exception("Column or row index out of range!")
		site = self.grid[row][col]
		if site.val is not None:
			return True
		return False

	# returns the number of open sites
	def numberOfOpenSites(self):
		return self.openCount;

	# does the system percolate?
	def percolates(self):
		top = self.wqu[n * n]
		bottom = self.wqu[(n * n) - 1]

		return top == bottom


