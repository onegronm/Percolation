from WeightedQuickUnionUF import WeightedQuickUnionUF

class Site:
	def __init__(self, i):
		self.open = False
		self.full = False
		self.val = i

class Percolation:
	
	# create n-by-n grid, with all sites initially blocked
	def __init__(self, n):

		if n <= 0:
			raise Exception("n must be greater than zero!")
		
		self.length = n

		self.wqu = WeightedQuickUnionUF((n * n) + 2) # two extra values for virtual top and bottom sites

		self.grid = [None] * n # maintain grid representation separate from wqu list
		
		for i in range (0, n):
			self.grid[i] = [None] * n

		self.openCount = 0 # keep track of open sites

		# create grid with site objects
		for i in range(0, n):
			for j in range(0, n):
				# find the index of site in wqu
				value = (i * n) + j

				# assign site object to grid in closed state
				site = Site(value)
				self.grid[i][j] = site

				# connect first row sites to top virtual site
				if i == 0:
					top = self.wqu.arr[n * n] # top site is the second to last in wqu list
					self.wqu.union(value, top)

				# connect last row sites with bottom virtual site
				if i == n - 1:
					bottom = self.wqu.arr[(n * n) + 1] # bottom site is the last in wqu list
					self.wqu.union(value, bottom)

	# opens the site (row, col) if it is not open
	def open(self, row, col):
		if row >= self.length or col >= self.length:
			raise Exception("Column or row index out of range!")

		site = self.grid[row][col]

		if not self.isOpen(row, col):
			site.open = True
			site.full = True
			self.openCount += 1

		# connect to all adjacent open sites:

		# connect top
		if row - 1 >= 0:
			top = self.grid[row - 1][col]

			# if the site is open and not previously connected
			if top.open and not self.wqu.connected(site.val, top.val):
				self.wqu.union(site.val, top.val) 
				top.full = True
				if self.percolates():
					return

		# connect right
		if col + 1 <= self.length - 1:
			right = self.grid[row][col + 1]

			# if the site is open and not previously connected
			if right.open and not self.wqu.connected(site.val, right.val):
				self.wqu.union(site.val, right.val)
				right.full = True
				if self.percolates():
					return

		# connect bottom
		if row + 1 <= self.length - 1:
			bottom = self.grid[row + 1][col]

			# if the site is open and not previously connected
			if bottom.open and not self.wqu.connected(site.val, bottom.val):
				self.wqu.union(site.val, bottom.val)
				bottom.full = True
				if self.percolates():
					return

		# connect left
		if col - 1 >= 0:
			left = self.grid[row][col - 1]

			# if the site is open and not previously connected
			if left.open and not self.wqu.connected(site.val, left.val):
				self.wqu.union(site.val, left.val)
				left.full = True
				if self.percolates():
					return
			

	# is the site (row, col) open?
	def isOpen(self, row, col):
		if row >= self.length or col >= self.length:
			raise Exception("Column or row index out of range!")
		site = self.grid[row][col]

		if site.open:
			return True

		return False

	# is the site (row, col) full?
	def isFull(self, row, col):
		if row >= self.length or col >= self.length:
			raise Exception("Column or row index out of range!")

		site = self.grid[row][col]
		
		return site.full

	# returns the number of open sites
	def numberOfOpenSites(self):
		return self.openCount;

	# does the system percolate?
	def percolates(self):
		#top = self.wqu.arr[self.length * self.length]
		#bottom = self.wqu.arr[(self.length * self.length) + 1]
		top = self.wqu.root(self.length * self.length)
		bottom = self.wqu.root((self.length * self.length) + 1)

		return top == bottom


