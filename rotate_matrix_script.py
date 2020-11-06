"""
        90 DEGREE ROTATE GIVEN MATRIX USING DYNAMIC MEMORY

"""


# it can be different just for instance
matrix = [[1,2,3],      
          [4,5,6],
          [7,8,9]]

def rotate_matrix(matrixArray):

    convert_zip = zip(*matrixArray[::-1])

    return [list(element) for element in convert_zip]

if __name__ == "__main__":

    print(rotate_matrix(matrix))