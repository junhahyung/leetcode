class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        self.matrix = matrix
        self.rowlen = len(matrix)
        self.collen = len(matrix[0])

        for i in range(self.rowlen):
            for j in range(self.collen):
                if matrix[i][j]:
                    self._update(i,j)

        return self.matrix

    def _update(self, i,j):
        maxdist = max(i, abs(self.rowlen -1 -i)) + max(j, abs(self.collen -1 -j))

        for m in range(maxdist):
            for k in range(m+2):
                a = k
                b = m-k+1
                if i+a >= 0 and i+a <= self.rowlen-1 and j+b >= 0 and j+b <= self.collen - 1:
                    if self.matrix[i+a][j+b]==0:
                        self.matrix[i][j] = m+1
                        return
                else:
                    pass
                if i-a >= 0 and i-a <= self.rowlen-1 and j+b >= 0 and j+b <= self.collen - 1:
                    if self.matrix[i-a][j+b]==0:
                        self.matrix[i][j] = m+1
                        return
                else:
                    pass
                if i+a >= 0 and i+a <= self.rowlen-1 and j-b >= 0 and j-b <= self.collen - 1:
                    if self.matrix[i+a][j-b]==0:
                        self.matrix[i][j] = m+1
                        return
                else:
                    pass
                if i-a >= 0 and i-a <= self.rowlen-1 and j-b >= 0 and j-b <= self.collen - 1:
                    if self.matrix[i-a][j-b]==0:
                        self.matrix[i][j] = m+1
                        return
                else:
                    pass
