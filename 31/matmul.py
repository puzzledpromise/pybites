class Matrix(object):

    def __init__(self, values):
        self.values = values
        self.nrows = len(self.values)
        self.ncols = len(self.values[0])

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        result = Matrix._init_mult_result(self,other) 
        
        for i in range(result.nrows):
            for j in range(result.ncols):
                Matrix._calc_entry(self, other, result, i, j)

        return result

    def __rmamtmul__(self, other):
        return other @ self

    def __imatmul__(self, other):
        return self @ other

    @staticmethod
    def _init_mult_result(mat1, mat2):
        """ Initialize the resulting matrix with proper dimensions."""
        result = []
        for r in range(mat1.nrows):
            row = []
            for c in range(mat2.ncols):
                row.append(0)
            result.append(row)

        return Matrix(result)

    @staticmethod
    def _calc_entry(mat1,mat2,result,i,j):
        #print(f"Calculating entry at {i}{j}:")
        #print()

        m = mat1.ncols
        calc = 0 
        for s in range(m):
           e = mat1.values[i][s] * mat2.values[s][j]
           #print(f"a{i}{s} * b{s}{j} = {e}")
           calc += e
        #print()
        #print(f"c{i}{j} = {calc}")
        #print()

        result.values[i][j] = calc
        

        


