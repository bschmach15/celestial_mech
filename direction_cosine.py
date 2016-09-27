from math import cos, sin, radians
import numpy as np

def rotation_matrix(x,y,z):
    x, y, z = radians(x), radians(y), radians(z)
    sin_x, cos_x = sin(x), cos(x)
    sin_y, cos_y = sin(y), cos(y)
    sin_z, cos_z = sin(z), cos(z)
    r_11 = cos_x * cos_y - sin_x * sin_y * cos_z
    r_12 = -cos_x * sin_y - sin_x * cos_y * cos_z
    r_13 = sin_x * sin_z
    r_21 = sin_x * cos_y + cos_x * sin_y * cos_z
    r_22 = - sin_x * sin_y + cos_x * cos_y * cos_z
    r_23 = -cos_x * sin_z
    r_31 = sin_y * sin_z
    r_32 = cos_y * sin_z
    r_33 = cos_z
    r = np.array([[r_11, r_12, r_13],[r_21, r_22, r_23],[r_31,r_32, r_33]])
    return r