class WeightedQuickUnionUF:

    def __init__(self, n):
        self.arr = [0] * n
        self.size = [0] * n

        for i in range(0, n):
            self.arr[i] = i;
            self.size[i] = 1;

    def root(self,p):
        while p != self.arr[p]:
            p = self.arr[p];

        return p;

    def connected(self,p,q):
        if self.arr[p] == self.arr[q]:
            return True;

        return False;

    def union(self,p,q):
        i = self.root(p)
        j = self.root(q)

        if self.size[i] <= self.size[j]:
            # p is smaller, so p is connecte to q
            self.arr[i] = j
            self.size[j] += self.size[i]
        else:
            # q is smaller, so q is connected to p
            self.arr[j] = i
            self.size[i] += self.size[j]

        n = len(self.arr)
        if self.size[i] == n or self.size[j] == n:
            return True;

        return False;




