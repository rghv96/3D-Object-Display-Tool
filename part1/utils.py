import numpy as np
from math import *

class Utils():
    # Transpose a matrix
    def transpose_matrix(self, matrix):
        return np.transpose(matrix)

    # Translate a point by dx, dy
    def translate_point(self, x, y, dx, dy):
        return x+dx, y+dy

    # Multiply two matrices together
    def matrix_multiply(self, matrix_a, matrix_b):
        return np.dot(matrix_a, matrix_b)

    # Rotate a matrix along the x-axis
    def rotate_along_x(self, x, matrix):
        return self.matrix_multiply([[1, 0, 0],
                                    [0, cos(x), -sin(x)], 
                                    [0, sin(x), cos(x)]], matrix)

    # Rotate a matrix along the y-axis
    def rotate_along_y(self, y, matrix):
        return self.matrix_multiply([[cos(y), 0, sin(y)], 
                                    [0, 1, 0], 
                                    [-sin(y), 0, cos(y)]], matrix)
    
    # Rotate a matrix along the z-axis
    def rotate_along_z(self, z, matrix):
        return self.matrix_multiply([[cos(z), sin(z), 0],
                                    [-sin(z), cos(z), 0], 
                                    [0, 0, 1]], matrix)

    # Get the diametrically opposite points of a point (x, y)
    # with a given radius
    def diametrically_opposite_points(self, x, y):
        radius = 5
        x1 = x - radius
        y1 = y - radius
        x2 = x + radius
        y2 = y + radius
        return x1, y1, x2, y2