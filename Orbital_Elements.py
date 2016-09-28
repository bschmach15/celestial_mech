import math

from Anomalies import Anomalies
import numpy as np
import constants
import scipy.constants
from Planets import Planets
from direction_cosine import rotation_matrix

class Orbital_Elements:

    def __init__(self, posistion = None, velocity = None, semi_parameter = None, eccentricity = None, inclination =
    None, right_ascension = None, perigee = None, true_anomaly = None):
        self.position = posistion
        self.velocity = velocity
        self.semi_parameter = semi_parameter
        self.eccentricity = eccentricity
        self.inclination = inclination
        self.right_ascension = right_ascension
        self.perigee = perigee
        self.true_anomaly = true_anomaly
        self.Earth = Planets("Earth", constants.earth_mass, constants.earth_radius)
        self.mu = 398600.4418 # scipy.constants.gravitational_constant * self.Earth._mass off by orders of mag
        self.semi_major_axis = None


    def calc_others(self):
        if self.position is not None and self.velocity is not None:
            self.pos_vel_to_orb_elements()
        if self.position is None and self.velocity is None:
            self.rotation = rotation_matrix(self.right_ascension, self.perigee, self.inclination)
            self.orb_elements_to_pos_vel()

    def pos_vel_to_orb_elements(self):
        angular_momentum = np.cross(self.position, self.velocity)
        angular_momentum_norm = np.linalg.norm(angular_momentum)
        node = np.cross(np.array([0,0,1]), angular_momentum)
        eccentricity_vector = ((np.linalg.norm(self.velocity)** 2 - (self.mu/np.linalg.norm(
            self.position))) * self.position - (np.dot(self.position,self.velocity)) * self.velocity)/(self.mu)
        self.eccentricity = np.linalg.norm(eccentricity_vector)
        specific_energy = 0.5 * np.linalg.norm(self.velocity)**2 - self.mu/np.linalg.norm(self.position)
        if self.eccentricity != 1.0:
            self.semi_major_axis = - self.mu/(2 * specific_energy)
            self.semi_parameter = self.semi_major_axis * (1 - self.eccentricity ** 2)
        else:
            self.semi_parameter = (angular_momentum_norm ** 2)/self.mu
            self.semi_major_axis = np.inf
        self.inclination = math.degrees(math.acos(angular_momentum[2]/angular_momentum_norm))
        self.right_ascension = math.degrees(math.acos(node[0]/np.linalg.norm(node)))
        if node[1] < 0:
            self.right_ascension = 360 - self.right_ascension
        self.perigee = math.degrees(math.acos(np.dot(node,eccentricity_vector)/(np.linalg.norm(node) * self.eccentricity)))
        self.true_anomaly = math.degrees(math.acos(np.dot(eccentricity_vector, self.position)/(self.eccentricity *
                                                                                               np.linalg.norm(
                                                                                               self.position))))
        if np.dot(self.position, self.velocity) < 0:
            self.true_anomaly = 360 - self.true_anomaly

    def orb_elements_to_pos_vel(self):
        pos_1 = (self.semi_parameter * math.cos(math.radians(self.true_anomaly)))/(1 + self.eccentricity * math.cos(
            math.radians(self.true_anomaly)))
        pos_2 = (self.semi_parameter * math.sin(math.radians(self.true_anomaly)))/(1 + self.eccentricity * math.cos(
            math.radians(self.true_anomaly)))
        vel_1 = - (math.sqrt(self.mu/self.semi_parameter)) * math.sin(math.radians(self.true_anomaly))
        vel_2 = (math.sqrt(self.mu/self.semi_parameter)) * (self.eccentricity + math.cos(math.radians(
            self.true_anomaly)))
        self.position = np.array([pos_1, pos_2, 0])
        self.velocity = np.array([vel_1, vel_2, 0])
        self.position = np.dot(self.rotation,self.position)
        self.velocity = np.dot(self.rotation,self.velocity)
        specific_energy = 0.5 * np.linalg.norm(self.velocity)**2 - self.mu/np.linalg.norm(self.position)
        self.semi_major_axis = - self.mu/(2 * specific_energy)


    def print_orb_elem(self):
        print("p = "  + str(self.semi_parameter))
        print("e = " + str(self.eccentricity))
        print("i = " + str(self.inclination))
        print("Omega = " + str(self.right_ascension))
        print("omega = " + str(self.perigee))
        print("nu = " + str(self.true_anomaly))

    def print_pos_vel(self):
        print("position = " + str(self.position))
        print("velocity = " + str(self.velocity))

    def calc_anomalies(self, mean_anomaly = None):
        if self.true_anomaly is not None:
            self.anomalies = Anomalies(self.eccentricity, self.semi_major_axis, true_anomaly = self.true_anomaly)
        else:
            self.anomalies = Anomalies(self.eccentricity, self.semi_major_axis, mean_anomaly = mean_anomaly)
            self.true_anomaly = self.anomalies

if __name__ == "__main__":
    position = np.array([6524.834,6862.875,6448.296])
    velocity = np.array([4.901327,5.533756,-1.976341])
    print(np.linalg.norm(position), np.linalg.norm(velocity))
    Orb_test_1 = Orbital_Elements(posistion=position, velocity = velocity)
    Orb_test_1.calc_others()
    Orb_test_1.print_orb_elem()

    Orb_test_2 = Orbital_Elements(semi_parameter=11067.790, eccentricity=0.83285, inclination=87.87,
                                  right_ascension=227.89, perigee=53.38, true_anomaly=92.335)
    Orb_test_2.calc_others()
    Orb_test_2.print_pos_vel()
    print(Orb_test_2.semi_major_axis)


    # ISS = Orbital_Elements(inclination= 51.6411, right_ascension=267.4531, eccentricity=0.0006512, perigee=9.1895)
    # ISS.calc_others()
    # ISS.calc_anomalies(mean_anomaly=350.9739)
    # ISS.print_pos_vel()
    # ISS.print_orb_elem()
