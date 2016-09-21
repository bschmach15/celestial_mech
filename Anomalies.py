import math
import scipy.constants as spc

class Anomalies:

    def __init__(self, eccentricity, semimajor_axis, planet = None, true_anomaly = None, mean_anomaly= None,
                 eccentric_anomaly = None, time_past_periapse = None):
        self.planet = planet
        self.eccentricity = eccentricity
        self.semimajor_axis = semimajor_axis
        self.true_anomaly = true_anomaly
        self.mean_anomaly = mean_anomaly
        self.eccentric_anomaly = eccentric_anomaly
        self.time_past_periapse = time_past_periapse
        if self.planet is not None:
            self.mean_motion = math.sqrt(spc.gravitational_constant * planet._mass/(self.semimajor_axis**3))
        self.main()

    def sec_to_min(self):
        self.time_past_periapse = self.time_past_periapse / 60

    def true_to_eccentric(self):
        true_anomaly_rads= math.radians(self.true_anomaly)
        self.eccentric_anomaly = math.degrees(2 * math.atan(math.sqrt((1. - self.eccentricity) / (1. + self.eccentricity)) * math.tan(true_anomaly_rads/ 2.)))
        if self.eccentric_anomaly < 0:
            self.eccentric_anomaly += 360

    def eccentric_to_true(self):
        ecc_anomaly_rads = math.radians(self.eccentric_anomaly)
        self.true_anomaly = math.degrees(2 * math.atan(math.sqrt((1. + self.eccentricity) / (1. - self.eccentricity)) * math.tan(ecc_anomaly_rads/ 2.)))
        if self.true_anomaly < 0:
            self.true_anomaly += 360

    def eccentric_to_mean(self):
        self.mean_anomaly = self.eccentric_anomaly - self.eccentricity * math.sin(math.radians(self.eccentric_anomaly))

    def mean_to_eccentric(self, tolerance = 1 * 10**(-8)):
        mean_anomaly_rads = math.radians(self.mean_anomaly)
        if spc.pi < mean_anomaly_rads < 0 or mean_anomaly_rads > spc.pi:
            E_current = mean_anomaly_rads - self.eccentricity
        else:
            E_current = mean_anomaly_rads + self.eccentricity
        difference = 1
        while abs(difference) > tolerance:
            E_previous = E_current
            E_current = E_previous + (mean_anomaly_rads - E_previous + self.eccentricity * math.sin(E_previous))/(1 -
                                                                                                                  self.eccentricity * math.cos(E_previous))
            difference = abs(E_current - E_previous)
        else:
            self.eccentric_anomaly = math.degrees(E_current)

    def mean_to_tpp(self):
        self.time_past_periapse = self.mean_anomaly / self.mean_motion
        self.sec_to_min()

    def tpp_to_mean(self):
        self.mean_anomaly = self.mean_motion * self.time_past_periapse * 60

    def eccentric_to_altitude(self):
        pass

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