import numpy as np
import math
from Planets import Planets
import scipy.constants as spc
import constants as c

"Problem 1"

class Anomalies:

    def __init__(self, planet, eccentricity, semimajor_axis, true_anomaly = None, mean_anomaly= None, eccentric_anomaly = None, time_past_periapse = None):
        self.planet = planet
        self.eccentricity = eccentricity
        self.semimajor_axis = semimajor_axis
        self.true_anomaly = true_anomaly
        self.mean_anomaly = mean_anomaly
        self.eccentric_anomaly = eccentric_anomaly
        self.time_past_periapse = time_past_periapse
        self.mean_motion = math.sqrt(spc.G * planet._radius/(self.semimajor_axis**3))

    def sec_to_min(self):
        self.time_past_periapse = self.time_past_periapse / 60

    def true_to_eccentric(self):
        true_anomaly_rads= math.radians(self.true_anomaly)
        self.eccentric_anomaly = math.degrees(2 * math.atan(math.sqrt((1. - self.eccentricity) / (1. + self.eccentricity)) * math.tan(true_anomaly_rads/ 2.)))

    def eccentric_to_true(self):
        ecc_anomaly_rads = math.radians(self.eccentric_anomaly)
        self.true_anomaly = math.degrees(2 * math.atan(math.sqrt((1. + self.eccentricity) / (1. - self.eccentricity)) * math.tan(self.eccentric_anomaly/ 2.)))

    def eccentric_to_mean(self):
        self.mean_anomaly = self.eccentric_anomaly - self.eccentricity * math.sin(math.radians(self.eccentric_anomaly))

    def mean_to_eccentric(self, tolerance = 1 * 10**(-8)):
        mean_anomaly_rads = math.radians(self.mean_anomaly)
        if (mean_anomaly_rads> spc.pi and mean_anomaly_rads< 0) or mean_anomaly_rads> spc.pi:
            E_current = mean_anomaly_rads- self.eccentricity
        else:
            E_current = mean_anomaly_rads + self.eccentricity
        difference = 1
        while abs(difference) > tolerance:
            E_previous = E_current
            E_current = E_previous + (mean_anomaly_rads- E_previous + self.eccentricity * math.sin(E_previous))/(1 - self.eccentricity * math.cos(E_previous))
            difference = abs(E_current - E_previous)
        else:
            self.eccentric_anomaly = math.degrees(E_current)

    def mean_to_tpp(self):
        self.time_past_periapse = self.mean_anomaly / self.mean_motion
        self.sec_to_min()

    def tpp_to_mean(self):
        self.mean_anomaly = self.mean_motion * self.time_past_periapse * 60

    def main(self):
        if self.true_anomaly is not None:
            self.true_to_eccentric()
            self.eccentric_to_mean()
            self.mean_to_tpp()
        elif self.eccentric_anomaly is not None:
            self.eccentric_to_true()
            self.eccentric_to_mean()
            self.mean_to_tpp()
        elif self.mean_anomaly is not None:
            self.mean_to_eccentric()
            self.eccentric_to_true()
            self.mean_to_tpp()
        elif self.time_past_periapse is not None:
            self.tpp_to_mean()
            self.mean_to_eccentric()
            self.eccentric_to_true()

if __name__ == "__main__":
    Earth = Planets("Earth", c.earth_mass, c.earth_radius)
    #Case A
    A = Anomalies(Earth, 0.15, 2. * Earth._radius, time_past_periapse=0)
    A.main()
    print("Case A:")
    print("True Anomaly: " + str(A.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(A.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(A.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(A.time_past_periapse) + " minutes")
    print("-------------------------------")
    B = Anomalies(Earth,.15,2.* Earth._radius, true_anomaly= 30.)
    B.main()
    print("Case B:")
    print("True Anomaly: " + str(B.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(B.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(B.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(B.time_past_periapse) + " minutes")
    print("-------------------------------")
    C = Anomalies(Earth,.15,2.* Earth._radius, eccentric_anomaly= 200.)
    C.main()
    print("Case C:")
    print("True Anomaly: " + str(C.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(C.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(C.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(C.time_past_periapse) + " minutes")
    print("-------------------------------")
    D = Anomalies(Earth,.15,2.* Earth._radius, true_anomaly= 90.)
    D.main()
    print("Case D:")
    print("True Anomaly: " + str(D.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(D.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(D.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(D.time_past_periapse) + " minutes")
    print("-------------------------------")
    E = Anomalies(Earth,.15,2.* Earth._radius, mean_anomaly= 270.)
    E.main()
    print("Case E:")
    print("True Anomaly: " + str(E.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(E.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(E.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(E.time_past_periapse) + " minutes")
    print("-------------------------------")
    F = Anomalies(Earth,.15,2.* Earth._radius, time_past_periapse= 25)
    F.main()
    print("Case F:")
    print("True Anomaly: " + str(F.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(F.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(F.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(F.time_past_periapse) + " minutes")
    print("-------------------------------")