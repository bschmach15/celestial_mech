import numpy as np
import math
import scipy.constants as spc
import constants

class Transfers:
    """r_initial = initial altitude
    r_final = final altitude"""

    def __init__(self):
        pass

    def holmann(self, r_initial, r_final):
        """delta_v is returned in km/s
        time_trans is returned in min"""
        a_trans = (r_initial + r_final)/2.0
        v_int = math.sqrt(constants.mu/r_initial)
        v_final = math.sqrt(constants.mu/r_final)
        v_trans_a = math.sqrt((2 * constants.mu)/r_initial - constants.mu/a_trans)
        v_trans_b = math.sqrt((2 * constants.mu)/r_final - constants.mu/a_trans)
        delta_v_a, delta_v_b = v_trans_a - v_int, v_final - v_trans_b
        delta_v = abs(delta_v_a) + abs(delta_v_b)
        time_trans = math.pi * math.sqrt((a_trans ** 3)/constants.mu)
        time_trans = time_trans / 60
        return delta_v, time_trans

    def bielliptic(self, r_initial,r_b, r_final):
        """delta_v returned in km/s
        time_trans returned in hours"""
        a_trans_1, a_trans_2 = (r_initial + r_b)/2, (r_b + r_final)/2
        v_initial, v_final = math.sqrt(constants.mu/r_initial), math.sqrt(constants.mu/r_final)
        v_trans_1_a = math.sqrt((2 * constants.mu)/r_initial - constants.mu/a_trans_1)
        v_trans_1_b = math.sqrt((2 * constants.mu)/r_b - constants.mu/a_trans_1)
        v_trans_2_b = math.sqrt((2 * constants.mu)/r_b - constants.mu/a_trans_2)
        v_trans_2_c = math.sqrt((2 * constants.mu)/r_final - constants.mu/a_trans_2)
        delta_v_a, delta_v_b, delta_v_c = v_trans_1_a - v_initial, v_trans_2_b - v_trans_1_b, v_final - v_trans_2_c
        delta_v = abs(delta_v_a) + abs(delta_v_b) + abs(delta_v_c)
        time_trans = math.pi * math.sqrt(a_trans_1 ** 3/constants.mu) + math.pi * math.sqrt(a_trans_2 ** 3/constants.mu)
        time_trans = time_trans / 3600
        return delta_v, time_trans



if __name__ == "__main__":
    transfers = Transfers()
    print(transfers.holmann(191.34411 + constants.earth_radius, 35781.34857 + constants.earth_radius))
    print(transfers.bielliptic(1.03 * constants.earth_radius, 80 * constants.earth_radius, 60 * constants.earth_radius))